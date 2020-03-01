### IMPORTS 

import json 
import nlp_lib as nlp

from igramscraper.instagram import Instagram
from google.cloud import firestore
from flask import jsonify

DB = firestore.Client()

### CONSTANTS
FIRESTORE_ID = 'export GCLOUD_PROJECT=poke-app-269623'
IG_SESSION_STORE = '/tmp/ig_temp'
USER_ID = None

ORGS_TABLE = u'Orgs'
JC_THRES = nlp.__jaccard_threshold__

### TEMP FUNCTIONS
#from .backend.db_entry import get_org, set_user

def get_user(uid):
    return DB.collection(u'Users').document(
        u'{}'.format(uid)).get().to_dict()

def set_user(uid, user_as_json):
    doc_ref = DB.collection(u'Users').document(uid)
    doc_ref.set(user_as_json)

### FUNCTIONS

def instagram_login_with_auth(uname, pwd):
	ig = Instagram()
	ig.with_credentials(uname, pwd, 
		IG_SESSION_STORE)

	ig.login()
	return ig

def get_recent_user_posts(uname, ig_obj):
	recent_posts = ig_obj.get_medias(uname, 5)

	posts_md = []
	for p in recent_posts:
		posts_md.append((p.created_time, p.caption, 
			p.image_high_resolution_url))

	return posts_md
"""
def check_poke_match(user, recent_posts):
	org_id = user['org_id']

	# get all org's pokes & user's completed pokes
	org = DB.collection(ORGS_TABLE).document(
        u'{}'.format(org_id)).get().to_dict()

	completed_pokes = user['complete_pokes_ids']
	org_pokes = org['poke_ids']

	# figure out valid pokes, pull pokes from db
	poke_ids_to_check = set(org_pokes) - set(
		completed_pokes)

	pokes_to_check = []
	for p in poke_ids_to_check:
		poke = DB.collection(u'Pokes').document(u'{}'.format(p)).get().to_dict()
		pokes_to_check.append(poke)
    # get similarity index between pokes and user
	for poke in pokes_to_check:
		poke_body = poke['body']

		for rp in recent_posts:
			ig_caption = rp[1]
			if npl.jaccard_similariy_index(poke_body, ig_caption) > JC_THRES: 
				return poke['pts']

	return None

def get_all_users():
	users = DB.collection(u'Users').stream()
	return [u.to_dict() for u in users]

def check_all_users(user_dicts):

	# get points each user has earned from completing pokes
	points_to_modify = []
	for ud in user_dicts:
		ig_auth = instagram_login_with_auth(
			ud['ig_uname'], ud['ig_pwd'])

		pts = None
		try:
			recent_posts = get_recent_user_posts(ig_auth)
			pts = check_poke_match(ud, recent_posts)
		except Exception as e:
			print(e)
		
		points_to_modify.append(pts)

	return points_to_modify

def modify_points(users, points):
	# add points to user dicts, upload to cloud
	for u, pts in zip(users, points):
		if pts is not None:
			u['pts'] += pts
		set_user(u['id'], u)

def function_entrypoint(request):
	users = get_all_users()
	points_to_modify = check_all_users(users)
	modify_points(users, points_to_modify)


def get_all_valid_pokes(user):
	org_id = user['org_id']

	# get all org's pokes & user's completed pokes
	org = DB.collection(ORGS_TABLE).document(
        u'{}'.format(org_id)).get().to_dict()

	completed_pokes = user['complete_pokes_ids']
	org_pokes = org['poke_ids']

	return set(org_pokes) - set(completed_pokes)
"""

def check_single_poke(user, poke_id):
	poke = DB.collection(u'Pokes').document(
		u'{}'.format(poke_id)).get().to_dict()

	ig_uname = user['user_credentials']['ig_uname']
	ig_pwd = user['user_credentials']['ig_pwd']

	ig_auth = instagram_login_with_auth(ig_uname, ig_pwd)
	recent_posts = get_recent_user_posts(ig_uname, ig_auth)

	if poke_id not in user['complete_pokes_ids']:
		poke_body = poke['data']['body']
		print('poke body:', poke_body)
		for rp in recent_posts:
			ig_caption = rp[1]
			print('ig_caption:', ig_caption)

			if nlp.jaccard_similariy_index(poke_body, ig_caption) > JC_THRES: 
				return poke['pts']

	return None 

def run_ig_single_poke_check(request):
	uid = request.args['uid']
	poke_id = request.args['poke_id']

	try:
		user = get_user(uid)
		pts = check_single_poke(uid, poke_id)
	except Exception as e:
		return jsonify(status='error', desc=str(e))
	
	if pts is not None:
		user['pts'] += pts
		user['complete_pokes_ids'].append(poke_id)
		set_user(uid, user)
		return jsonify(status='success', desc='valid_ig_poke_check')

"""
if __name__ == '__main__':
	user = get_user('1076440981d44efb')
	print(user)
	print(check_single_poke(user, 'test'))
"""



	


