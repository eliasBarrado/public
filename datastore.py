from google.cloud import datastore

import configparser

config = configparser.ConfigParser()
config.read('config.txt')

client = datastore.Client(project=config['project']['id'])

def getLastID():
	key = client.key('Time', 'last')
	lastID = client.get(key)
	return lastID['id']


def setLastID(lastID):
	key = client.key('Time', 'last')
	entity = datastore.Entity(key=key)
	entity.update({'id':lastID})
	client.put(entity)

	key = client.key('Time', lastID)
	entity = datastore.Entity(key=key)
	entity.update({'id':lastID})
	client.put(entity)


	