import keys
import json, httplib, urllib

def get_connection():
	con = httplib.HTTPSConnection('api.parse.com', 443)
	con.connect()
	return con

def make_parse_get_request(url, params={}):
	connection = get_connection()
	params = urllib.urlencode(params)
	connection.request(
		'GET',
		url + '?%s' % params,
		'',
		{
			"X-Parse-Application-Id": keys.PARSE_APP_ID,
			"X-Parse-REST-API-Key": keys.PARSE_REST_API_KEY
		}
	)
	result = json.loads(connection.getresponse().read())
	return result

def make_parse_post_request(url, obj):
	connection = get_connection()
	connection.request(
		'POST',
		url,
		json.dumps(obj),
		{
			"X-Parse-Application-Id": keys.PARSE_APP_ID,
			"X-Parse-REST-API-Key": keys.PARSE_REST_API_KEY
		}
	)
	result = json.loads(connection.getresponse().read())
	return result

def make_parse_put_request(url, obj):
	connection = get_connection()
	connection.request(
		'PUT',
		url,
		json.dumps(obj),
		{
			"X-Parse-Application-Id": keys.PARSE_APP_ID,
			"X-Parse-REST-API-Key": keys.PARSE_REST_API_KEY
		}
	)
	result = json.loads(connection.getresponse().read())
	return result

def make_parse_delete_request(url, obj):
	connection = get_connection()
	connection.request(
		'DELETE',
		url,
		'',
		{
			"X-Parse-Application-Id": keys.PARSE_APP_ID,
			"X-Parse-REST-API-Key": keys.PARSE_REST_API_KEY
		}
	)
	result = json.loads(connection.getresponse().read())
	return result