class KrakenOHLC:
	def __init__(self, krakenOHLC):
		self.error  = krakenOHLC['error']
		self.result = krakenOHLC['result']
		self.last   = krakenOHLC['result']['last']
		self.krakenOHLC = krakenOHLC

	def getLast(self):
		return self.last

	def hasError(self):
		if(self.error != []):
			return False

		return True

	def getCommited(self):
		commitedOHLC = [x for x in self.result['XXBTZUSD'] if x[0] <= self.last]
		return commitedOHLC

	def getOriginal(self):
		return self.krakenOHLC



