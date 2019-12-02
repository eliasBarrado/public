import time
import krakenex
import configparser
import datastore
import bigquery

from model import KrakenOHLC

#config = configparser.ConfigParser()
#config.read('config.txt')

#k = krakenex.api.API(config['public']['key'], config['public']['secret'])
k = krakenex.api.API()

def run():
	while(True):
		
		time.sleep(20)

		print('Retrieving last ID stored in BigQuery from Datastore:')
		last = datastore.getLastID()

		print('Last ID in Datastore is {}'.format(last))

		print('Querying last OHLC data to Kraken:')
		
		krakenOHLC = KrakenOHLC.KrakenOHLC(k,'XXBTZUSD',since=last)

		if(krakenOHLC.hasError()):
			continue
		
		print('OHLC from Kraken:\n', krakenOHLC.getOriginal())

		print('Last ID from Kraken OHLC data is {}'.format(krakenOHLC.getLast()))
		
		if(last != krakenOHLC.getLast()):
			if(bigquery.insertOHLC(krakenOHLC)):
				last = krakenOHLC.getLast()
				datastore.setLastID(last)
		print('==================================================================')				
		

		




