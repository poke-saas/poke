### IMPORTS 

import json 

import requests
from igramscraper.instagram import Instagram

### CONSTANTS
IG_SESSION_STORE = '/tmp/ig_temp'

def import_user_token(debug=False, debug_path=None):
	if debug:
		with open(debug_path, 'r') as json_file:
    		return json.load(data, outfile)
    else:
    	#todo: integrate with db
    	pass

def instagram_login_with_auth(uname, pwd):
	ig = Instagram()
	ig.with_credentials(uname, pwd, 
		IG_SESSION_STORE)

	ig = Instagram()
	ig.login()
	return ig

