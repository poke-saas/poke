### IMPORT
from google.cloud import firestore
import uuid

### CONSTANTS
FIRESTORE_ID = 'export GCLOUD_PROJECT=poke-app-269623'
DB = firestore.Client() 

USERS_TABLE = u'Users'
DEFAULT_USER = u'user_model'

ORGS_TABLE = u'Orgs'
DEFAULT_ORG = u'orgs_model'

def get_orgs_template():
	template = DB.collection(ORGS_TABLE).document(
		DEFAULT_ORG).get().to_dict()

	template['user_ids'].pop()
	template['rewards_ids'].pop()
	template['poke_ids'].pop()
	return template

def get_user_template():
	template = DB.collection(USERS_TABLE).document(
		DEFAULT_USER).get().to_dict()

	template['complete_pokes_ids'].pop()
	return template

def new_user_obj():
	new_uid = uuid.uuid4().hex[:16]
	new_user = get_user_template()
	new_user['id'] = new_uid
	return new_uid, new_user

def add_new_user():
	new_uid, new_user = new_user_obj()
	set_user(new_uid, new_user)
	return new_uid

def get_user(uid):
	return DB.collection(USERS_TABLE).document(
		u'{}'.format(uid)).get().to_dict()

def set_user(uid, user_as_json):
	doc_ref = DB.collection(USERS_TABLE).document(uid)
	doc_ref.set(user_as_json)
	
"""
if __name__ == '__main__':
"""

