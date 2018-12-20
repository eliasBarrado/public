import time
import logging

def getServerTime(k):
	try:
		response = k.query_public('Time')
		logging.info(response)

	except Exception as error:
		logging.error(error)
		time.sleep(2)
		response = getServerTime(k)

	return response

def getTickerInformation(k, pair):
	try:
		response = k.query_public('Ticker', {'pair': pair})

	except Exception as error:
		time.sleep(2)
		getTickerInformation(k, pair)

	return response

def getOHLCData(k, pair, interval=1, since=None):
	try:
		response = k.query_public('OHLC', {'pair': pair, 'interval': interval, 'since': since})

	except Exception as error:
		time.sleep(2)
		getOHLCData(k,pair,interval,since)

	return response