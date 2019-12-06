import time
import krakenex
import configparser
import datastore
import bigquery
import log
from model import KrakenOHLC

logger = log.getLogger(__name__)
#config = configparser.ConfigParser()
#config.read('config.txt')

#k = krakenex.api.API(config['public']['key'], config['public']['secret'])
k = krakenex.api.API()



def run():
	while(True):
		
		time.sleep(20)

		logger.info('Retrieving last ID stored in BigQuery from Datastore:')
		last = datastore.getLastID()

		logger.info('Last ID in Datastore is {}'.format(last))

		logger.info('Querying last OHLC data to Kraken:')
		
		krakenOHLC = KrakenOHLC.KrakenOHLC(k,'XXBTZUSD',since=last)

		if(krakenOHLC.hasError()):
			logger.error(krakenOHLC.getError())
			continue
		
		logger.info('OHLC from Kraken: {}\n'.format(krakenOHLC.getOriginal()))

		logger.info('Last ID from Kraken OHLC data is {}'.format(krakenOHLC.getLast()))
		
		if(last != krakenOHLC.getLast()):
			if(bigquery.insertOHLC(krakenOHLC)):
				last = krakenOHLC.getLast()
				datastore.setLastID(last)
		
		logger.info('==================================================================')				
		

		




