import time

def getServerTime(k, unixtime=True):
	try:
		response = k.query_public('Time')

	except Exception as error:
		time.sleep(2)
		getServerTime(k)
	
	if(unixtime):
		return response['result']['unixtime']

	return response['result']['rfc1123']

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