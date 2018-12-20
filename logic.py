import time
import krakenex
import public

k = krakenex.api.API()

def run():
	while(True):
		print('Querying serverTime to Kraken:')
		serverTime = public.getServerTime(k)
		print(serverTime)
		time.sleep(10)


