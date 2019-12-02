from google.cloud import bigquery

import configparser
import logging

config = configparser.ConfigParser()
config.read('config.txt')

client = bigquery.Client(project=config['project']['id'])

dataset_id = 'kraken'
table_id   = 'OHLC'
table_ref  = client.dataset(dataset_id).table(table_id)
table      = client.get_table(table_ref)  

def insertOHLC(krakenOHLC):
	rows_to_insert = krakenOHLC.getCommited()
	errors = client.insert_rows(table, rows_to_insert)
	
	if(errors != []):
		logging.error(errors)
		return False

	return True
