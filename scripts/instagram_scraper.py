### IMPORTS 

import json 

import requests
from igramscraper.instagram import Instagram
#from google.cloud import datastore
from google.cloud import firestore

### CONSTANTS
FIRESTORE_ID = 'export GCLOUD_PROJECT=poke-app-269623'
IG_SESSION_STORE = '/tmp/ig_temp'
DEBUG_CRED_PATH = '/Users/michaelusachenko/Desktop/poke/cred/test_ig_credentials.json'

def import_user_token(debug=False, debug_path=None):
	if debug:
		with open(debug_path, 'r') as json_file:
			return json.load(json_file)
	else:
		# todo: call db
		pass

def ig_cache_reader(options=None):
	pass

def instagram_login_with_auth(uname, pwd):
	ig = Instagram()
	ig.with_credentials(uname, pwd, 
		IG_SESSION_STORE)

	ig.login()
	return ig

def get_recent_user_posts(ig_obj):
	recent_posts = ig_obj.get_medias(uname, 5)

	posts_md = []
	for p in recent_posts:
		posts_md.append((p.created_time, p.caption, 
			p.image_high_resolution_url))

	return posts_md

def get_user_posts_demo():
	ut = import_user_token(debug=True, 
		debug_path=DEBUG_CRED_PATH)

	uname, pwd = ut['uname'], ut['pwd']
	ig_auth = instagram_login_with_auth(uname, pwd)
	print(get_recent_user_posts(ig_auth))




