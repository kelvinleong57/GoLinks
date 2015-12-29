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
	# decode from encoded version on Parse
	decoded_key = urllib2.quote(key, 'utf-8')

	params = {'where': json.dumps({'key': decoded_key})}
	golinks = ParseDriver.make_parse_get_request('/1/classes/ParseGoLink', params)['results']
	
	if len(golinks) == 0:
		return 'not a valid key'
	else:
		# decode from encoded version on Parse
		decoded_url = urllib2.unquote(golinks[0]['url'])
		return redirect(decoded_url)

@app.route('/create_golink', methods=['POST'])
def create_golink():
	golink = {	'key': request.form['key'],
				'url': request.form['url'] }

	ParseDriver.make_parse_post_request('/1/classes/ParseGoLink', golink)
	return 'ok'

@app.route('/lookup', methods=['GET'])
def lookup():
	params = {'where': json.dumps({'url': request.form['url']})}

	golinks = ParseDriver.make_parse_get_request('/1/classes/ParseGoLink', params)['results']
	if len(golinks) == 0:
		return 'No previous go-links found'
	else:
		return golinks[0]['keys']