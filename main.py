from flask import Flask
import logic

app = Flask(__name__)

@app.route('/_ah/start')
def start():
	print('Call to /_ah/start')
	logic.run()

  
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
   

