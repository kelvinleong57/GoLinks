# Go-Links

Keyword-based bookmarking within the search bar, initiated with the word *go*. Enables users to easily share any bookmarked websites (called *go-links*) by simply distributing the keyword it was marked with. All users require the accompanying Chrome extension; the link is below in the [Getting Started](#getting-started) section.

This repository is the Flask backend that handles all of the HTTP GET and POST requests to Parse, the database containing all of the data. It also contains the files for local testing.

## Usage

Follow the instructions in the Chrome extension repository to install it. Usage instructions are there as well.
  - https://github.com/kelvinleong57/chrome-go-links
  - currently requires running a local Flask server to work (see [below](#setting-up-to-develop))

## Setting Up to Develop
1. Clone this repo
    - https://github.com/kelvinleong57/go-links
2. Run `pip install Flask==0.9`
    - Flask v0.10 has been untested with this application, so just stick with Flask v0.9 first
3. Create keys.py by filling out keys-example.py
    - the Parse keys are found at https://parse.com/apps/golinks--2/
4. Run the Flask server
    - on Terminal, run `python runserver.py` from the root directory
5. Visit `localhost:5000/` to get started

## Dependencies
  - Flask v0.9 
  - Parse database

## Files
To ensure scalability, files and folders have been structured into packages, as opposed to modules. The package is named **golinks**.
### routes.py
handles the logic for making the Parse requests for go-links, including redirecting go-links

has the following functions/routes:
```python
@app.route('/go/<key>')
def go(key):
  # given a key, user will be redirected to the corresponding URL bookmarked with that key, if applicable

@app.route('/create_golink', methods=['POST'])
def create_golink():
  # upon an POST request, creates a go-link with the request.form's key and URL (both encoded) and pushes this to Parse
```
### parse_driver.py
handles all of the Parse GET and POST requests

for each request, you need to pass in the URL (e.g. `'/1/classes/ParseGoLink'`) as well as a dictionary of parameters, varying with GET or POST request
```python
# GET request
params = {'where': json.dumps({'key': decoded_key})}

# POST request (params is the go-link to POST)
golink = {	'key': request.form['key'],
			'url': request.form['url'] }
```

## Resources
  - [David Liu](https://github.com/davidbliu) - my Fall 2015 Web Development Committee Chair for [Berkeley PBL](http://www.berkeleypbl.com/) 
    - https://github.com/davidbliu/flask-portal
    - https://github.com/davidbliu/pbl-link-extension
    - https://github.com/davidbliu/pbl-portal-new