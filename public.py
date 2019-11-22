import time
import logging

def getServerTime(k):
	try:
		response = k.query_public('Time')
	except Exception as error:
		logging.error(error)
		time.sleep(2)
		response = getServerTime(k)

	return response

def getTickerInformation(k, pair):
	try:
		response = k.query_public('Ticker', {'pair': pair})
	except Exception as error:
		logging.error(error)
		time.sleep(2)
		response = getTickerInformation(k, pair)

	return response

def getOHLC(k, pair, interval=5, since=None):
	'Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always be present, regardless of the value of "since"'
	if(since != None):
		since = str(since)
	try:
		response = k.query_public('OHLC', {'pair': pair, 'interval': interval, 'since': since})
		if(response['error'] != []):
			logging.error(response['error'])
			time.sleep(2)
			response = getOHLC(k,pair,interval,since)

	except Exception as error:
		logging.error(error)
		time.sleep(2)
		response = getOHLC(k,pair,interval,since)

	return response

