# Go-Links

Keyword-based bookmarking within the search bar, initiated with the word *go*. Enables users to easily share any bookmarked websites (called *go-links*) by simply distributing the keyword it was marked with. All users require the accompanying Chrome extension; the link is below in the [Getting Started](#getting-started) section.

This repository is the Flask backend that handles all of the HTTP GET and POST requests to Parse, the database containing all of the data. It also contains the files for local testing.

## Getting Started

Follow the instructions in the Chrome extension repository to install it.
  - https://github.com/kelvinleong57/chrome-go-links

## Dependencies
  - Flask v0.9 
  - Parse database

## Files
To ensure scalability, files and folders were structured as packages. Package is named **golinks**, and the program is run by calling `python runserver.py` on the terminal.
### runserver.py
Its only job is to choose the port number and run the application. It has been split off from the package for structure's sake.
### routes.py
Handles the logic for making the Parse requests for go-links. Also is what the website that directs go-links.
### parse_driver.py
Handles all of the Parse GET and POST requests

## Resources
  - [David Liu](https://github.com/davidbliu) - my Fall 2015 Web Development Committee Chair for [Berkeley PBL](http://www.berkeleypbl.com/) 
    - https://github.com/davidbliu/flask-portal
    - https://github.com/davidbliu/pbl-link-extension
    - https://github.com/davidbliu/pbl-portal-new