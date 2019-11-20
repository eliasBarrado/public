from google.cloud import bigquery

import configparser

config = configparser.ConfigParser()
config.read('config.txt')

client = bigquery.Client(project=config['project']['id'])

dataset_id = 'kraken'
table_id   = 'OHLC'
table_ref  = client.dataset(dataset_id).table(table_id)
table      = client.get_table(table_ref)  # API request

def insertOHLC(ohlc):
	return True
"""
rows_to_insert = [
    (u'Phred Phlyntstone', 32),
    (u'Wylma Phlyntstone', 29),
]

errors = client.insert_rows(table, rows_to_insert)  # API request

assert errors == []
"""