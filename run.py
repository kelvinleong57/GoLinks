import keys

from flask import Flask, request, jsonify, render_template, redirect, url_for, session, Response, make_response
from flask.ext.cors import CORS
import sys, json, datetime

# Kelvin
import parse_driver as ParseDriver

app = Flask(__name__)
app.config.from_pyfile('config.py')
CORS(app)

# *********************** ROUTES ***********************

@app.route('/')
def hello():
	return 'Kelvin Leong website'

@app.route('/test')
def test_route():
	return 'testing'

@app.route('/render_template')
def test_route():
	render_template('index.html')
	return 'ok'

# *********************** GO LINKS ***********************

@app.route('/go/<key>')
def go(key):
	params = {'where': json.dumps({'key': key})}
	golinks = ParseDriver.make_parse_get_request('/1/classes/ParseGoLink', params)['results']
	if len(golinks) == 0:
		return 'not a valid key'
	else:
		return redirect(golinks[0]['url'])

@app.route('/create_golink', methods=['POST'])
def create_golink():
	# form = request.get_json()
	# golink = {	'key': form.get('key'),
				# 'url': form.get('url') }

	golink = {	'key': 'asdasd',
				'url': 'asdasdasd' }

	ParseDriver.make_parse_post_request('/1/classes/ParseGoLink', golink)
	return 'ok'

# *********************** LOGIC ***********************

if __name__ == "__main__":
	try:
		port = int(sys.argv[1])
		app.run(host='0.0.0.0', port=port, debug=False)
	except:
		port = 3000
		app.run(host='0.0.0.0', port=port, debug=True)