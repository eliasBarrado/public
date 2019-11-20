import time
import krakenex
import public
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
		"""
		print('Querying server time to Kraken:')
		serverTime = public.getServerTime(k)
		print(serverTime)

		print('Querying ticker information to Kraken:')
		ticker = public.getTickerInformation(k,'XXBTZUSD')
		print(ticker)
		if(verify(ticker)):
			datastore.putTicker(ticker)

		"""
		print('Retrieving last ID stored in BigQuery from Datastore:')
		last = datastore.getLastID()

		print('Last ID in Datastore is {}'.format(last))

		print('Querying last OHLC data to Kraken:')
		
		krakenOHLC = KrakenOHLC.KrakenOHLC(public.getOHLC(k,'XXBTZUSD',since=last))
		'Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always be present, regardless of the value of "since"'
		print('OHLC from Kraken:\n', krakenOHLC.getOriginal())

		print('Last ID from Kraken OHLC data is {}'.format(krakenOHLC.getLast()))

		if(last != krakenOHLC.getLast()):
			success = bigquery.insertOHLC(krakenOHLC)
			if(success):
				last = krakenOHLC.getLast()
				datastore.setLastID(last)
		print('==================================================================')				


		time.sleep(20)


def verify(ticker):
	if(ticker['error'] != []):
		return False

	return True

