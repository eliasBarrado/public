from google.cloud import datastore

"""
import configparser

config = configparser.ConfigParser()
config.read('config.txt')

client = datastore.Client(project=config['project']['id'])

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

"""

def getLastID():
	return True

def setLastID():
	return True