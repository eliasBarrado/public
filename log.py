from google.cloud import logging as cloudlogging
import logging

def getLogger(name):
	log_client = cloudlogging.Client()

	log_handler = log_client.get_default_handler()

	cloud_logger = logging.getLogger(name)
	
	cloud_logger.setLevel(logging.INFO)
	cloud_logger.addHandler(log_handler)

	return cloud_logger


