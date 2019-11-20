class OHLC:
	
	def __init__(self, ohlc):
		self.time  = ohlc[0]
		self.open  = float(ohlc[1])
		self.high  = float(ohlc[2])
		self.low   = float(ohlc[3])
		self.close = float(ohlc[4])
		self.vwap  = float(ohlc[5])
		self.count = int(ohlc[6])