import keys

from flask import Flask, request, jsonify, render_template, redirect, url_for, session, Response, make_response
# from flask.ext.cors import CORS
import sys, json, datetime
import urllib2

# Kelvin
import parse_driver as ParseDriver

from golinks import app

# app = Flask(__name__)
# app.config.from_pyfile('config.py')
# CORS(app)

# *********************** ROUTES ***********************

@app.route('/')
@app.route('/go')
def index():
	return render_template('index.html', name='Kelvin')

@app.route('/test')
def test_route():
	return 'testing'

# *********************** GO LINKS ***********************

@app.route('/go/<key>')
def go(key):
	params = {'where': json.dumps({'key': key})}

	# Parse GET request will already encode the params, so no need to encode twice
	golinks = ParseDriver.make_parse_get_request('/1/classes/ParseGoLink', params)['results']
	
	if len(golinks) == 0:
		return 'Not a valid key'
	else:
		# decode from encoded version from Parse
		decoded_url = urllib2.unquote(golinks[0]['url'])
		return redirect(decoded_url)

@app.route('/create_golink', methods=['POST'])
def create_golink():
	# POST request will not encode, so ensure these are already encoded

	golink = {	'key': request.form['key'],
				'url': request.form['url'] }

	ParseDriver.make_parse_post_request('/1/classes/ParseGoLink', golink)
	return 'ok'

@app.route('/lookup')
def lookup():
	try:
		# URL should already be encoded
		url = request.args.get('url', '')
	except KeyError:
		# may want to return an empty JSON instead
		return 'No key found in the lookup function'

	params = {'where': json.dumps({'url': url})}
	golinks = ParseDriver.make_parse_get_request('/1/classes/ParseGoLink', params)['results']

	matching_golinks = []
	# check for multiple go-links that map to same URL
	for g in golinks:
		decoded_key = urllib2.unquote(g['key'])
		matching_golinks.append(decoded_key)

	return json.dumps(matching_golinks)