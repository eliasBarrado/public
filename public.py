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


