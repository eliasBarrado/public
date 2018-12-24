from google.cloud import datastore
import time

client = datastore.Client(project='')

def putTicker(ticker):
	key    = client.key('Ticker', 'last')
	entity = tickerToEntity(ticker, key)
	client.put(entity)

	key    = client.key('Ticker', int(time.time()))
	entity = tickerToEntity(ticker, key)
	client.put(entity)

def tickerToEntity(ticker, key):
	entity = datastore.Entity(key=key)
	for x in ticker['result']['XXBTZUSD']:
		entity[x] = ticker['result']['XXBTZUSD'][x]

	return entity