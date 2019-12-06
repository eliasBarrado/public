from flask import Flask
import logic
import log

logger = log.getLogger(__name__)

app = Flask(__name__)

@app.route('/_ah/start')
def start():
	logger.info('Call to /_ah/start')
	logic.run()

  
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
   

