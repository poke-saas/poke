### IMPORTS
import uuid
import hashlib

from google.cloud import firestore

### CONSTANTS
FIRESTORE_ID = 'export GCLOUD_PROJECT=poke-app-269623'
DB = firestore.Client() 

DUMMY_UUID = '4bec29754ace435f'

USERS_TABLE = u'Users'
DEFAULT_USER = u'user_model'

ORGS_TABLE = u'Orgs'
DEFAULT_ORG = u'orgs_model'

USER_CRED = 'user_credentials'
def get_db():
	return DB

def get_orgs_template():
	template = DB.collection(ORGS_TABLE).document(
		DEFAULT_ORG).get().to_dict()

S_FACEBOOK = 0
S_INSTAGRAM = 1
S_TWITTER = 2
S_LINKEDIN = 3

### ABSTRACT OPERATORS

def get():
	pass

def set(loc, id, data):
	doc_ref = DB.collection(loc).document(uid)
	doc_ref.set(data)

def new(new_fn, set_fn):
	new_id, new_obj = new_fn()
	set_fn(new_id, new_obj)
	return new_id

def add():
	pass

def rm():
	pass

### HELPERS 

# hold encryption key in env vars of function
# todo 
def encrypt_string(to_encrypt):
	pass

def hash_string_sha256(to_hash):
	m = hashlib.sha256()
	m.update(to_hash.encode())
	return m.hexdigest()

### USER HELPER METHODS
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

def get_user(uid):
	return DB.collection(USERS_TABLE).document(
		u'{}'.format(uid)).get().to_dict()

def set_user(uid, user_as_json):
	doc_ref = DB.collection(USERS_TABLE).document(uid)
	doc_ref.set(user_as_json)

def add_new_user():
	new_uid, new_user = new_user_obj()
	set_user(new_uid, new_user)
	return new_uid

def rm_user(uid):
	DB.collection(USERS_TABLE).document(uid).delete()

### ORGS OBJECT MODFIER METHODS
def add_social_integration(uid, s_type, s_uname, s_pwd):
	user = get_user(uid)
	hash_uname = hash_string_sha256(s_uname)
	hash_pwd = hash_string_sha256(s_pwd)

	if s_type == S_FACEBOOK:
		user[USER_CRED]['fb_uname'] = hash_uname
		user[USER_CRED]['fb_pwd'] = hash_pwd
	elif s_type == S_INSTAGRAM:
		user[USER_CRED]['ig_uname'] = hash_uname
		user[USER_CRED]['ig_pwd'] = hash_pwd
	elif s_type == S_TWITTER:
		user[USER_CRED]['twitter_uname'] = hash_uname
		user[USER_CRED]['twitter_pwd'] = hash_pwd
	elif s_type == S_LINKEDIN:
		user[USER_CRED]['linkedin_uname'] = hash_uname
		user[USER_CRED]['linkedin_pwd'] = hash_pwd

	set_user(uid, user)

def add_complete_poke(uid, poke_id):
	user = get_user(uid)
	user['complete_pokes_ids'].append(poke_id)
	set_user(uid, user)

# todo: inline from davis
def add_claimed_reward():
	user = get_user(uid)
	user['complete_pokes_ids'].append(poke_id)
	set_user(uid, user)

def add_user_fullname_and_profile_pic(uid, name, plink):
	user = get_user(uid)
	user['full_name'] = name
	user['profile_picture_link'] = plink
	set_user(uid, user)

### ORGS HELPER METHODS
def get_orgs_template():
	template = DB.collection(ORGS_TABLE).document(
		DEFAULT_ORG).get().to_dict()

	template['user_ids'].pop()
	template['reward_ids'].pop()
	template['poke_ids'].pop()
	template['name'] = str()
	return template

def new_org_obj():
	new_uid = uuid.uuid4().hex[:16]
	new_org = get_orgs_template()
	new_org['id'] = new_uid
	return new_uid, new_org

def get_org(oid):
	return DB.collection(ORGS_TABLE).document(
		u'{}'.format(oid)).get().to_dict()

def set_org(oid, org_as_json):
	doc_ref = DB.collection(ORGS_TABLE).document(oid)
	doc_ref.set(user_as_json)

def add_new_org():
	new_uid, new_org = new_org_obj()
	set_org(new_uid, new_org)
	return new_uid

def rm_org(oid):
	DB.collection(ORGS_TABLE).document(oid).delete()

### ORGS OBJECT MODFIER METHODS
def add_org_name(oid, name):
	org = get_org(oid)
	org['name'] = name
	set_org(oid, org)

def add_org_media():
	pass

def add_org_user(uid, user_ref):
	org = DB.collection(ORGS_TABLE).document(uid).get().to_dict()
	user = DB.collection(USERS_TABLE).document(user_ref).get().to_dict()
	org['user_ids'].append(user['id'])
	set_org(uid, org)

def add_org_poke(oid, poke_id):
	org = get_org(oid)
	org['poke_ids'].append(poke_id)
	set_org(oid, org)

def add_org_reward(oid, reward_id):
	org = get_org(oid)
	org['rewards_ids'].append(reward_id)
	set_org(oid, org)

def rm_org_poke(oid, poke_id):
	org = get_org(oid)
	rm_idx = None
	pids = org['poke_ids']

	for idx, p in enumerate(pids):
		if p == poke_id:
			rm_idx = idx
			break

	if rm_idx is not None:
		pids.pop(rm_idx)
	else:
		pass
		# todo handle errors

	org['poke_ids'] = pids
	set_org(oid, org)

def rm_org_reward():
	pass

### POKE HELPER METHODS
def get_poke_template():
	pass

def get_poke():
	pass

def set_poke():
	pass

def add_poke():

def rm_poke(id):

	pass


if __name__ == '__main__':
	pass
