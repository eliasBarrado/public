import time
import krakenex
import public
import datastore

k = krakenex.api.API()

def run():
	while(True):
		print('Querying server time to Kraken:')
		serverTime = public.getServerTime(k)
		print(serverTime)

		print('Querying ticker information to Kraken:')
		ticker = public.getTickerInformation(k,'XXBTZUSD')
		print(ticker)
		if(verify(ticker)):
			datastore.putTicker(ticker)


		print('Querying OHLC data to Kraken:')
		ohlc = public.getOHLC(k,'XXBTZUSD')
		print(ohlc)

		time.sleep(20)


def verify(ticker):
	if(ticker['error'] != []):
		return False

	return True

