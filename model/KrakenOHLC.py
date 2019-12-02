class KrakenOHLC:
	def __init__(self, k, pair, interval=5, since=None):

		'Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always be present, regardless of the value of "since"'
		if(since != None):
			since = str(since)
		try:
			response = k.query_public('OHLC', {'pair': pair, 'interval': interval, 'since': since})
			self.error  = response['error']
			self.result = response['result']
			self.last   = response['result']['last']
			self.krakenOHLC = response

		except Exception as error:
			logging.error(error)

		

	def getLast(self):
		return self.last

	def hasError(self):
		try:
			return self.error != []
		except Exception as error:
			return True

	def getCommited(self):
		commitedOHLC = [x for x in self.result['XXBTZUSD'] if x[0] <= self.last]
		return commitedOHLC

	def getOriginal(self):
		return self.krakenOHLC



