### IMPORTS 
import hashlib
from flask import jsonify
from google.cloud import firestore

### CONSTANTS
S_FACEBOOK = 0
S_INSTAGRAM = 1
S_TWITTER = 2
S_LINKEDIN = 3
USER_CRED = 'user_credentials'
DB = firestore.Client()

def get_user(uid):
    return DB.collection(u'Users').document(
        u'{}'.format(uid)).get().to_dict()

def set_user(uid, user_as_json):
    doc_ref = DB.collection(u'Users').document(uid)
    doc_ref.set(user_as_json)

def hash_string_sha256(to_hash):
    m = hashlib.sha256()
    m.update(to_hash.encode())
    return m.hexdigest()

def add_social_integration(request):
    uid = request.args['uid']
    s_type = request.args['s_type']
    s_uname = request.args['s_uname']
    s_pwd = request.args['s_pwd']

    user = get_user(uid)
    s_type = int(s_type)

    #hash_uname = hash_string_sha256(s_uname)
    #hash_pwd = hash_string_sha256(s_pwd)

    if s_type == S_FACEBOOK:
        user[USER_CRED]['fb_uname'] = s_uname #hash_uname
        user[USER_CRED]['fb_pwd'] = s_pwd #hash_pwd
    elif s_type == S_INSTAGRAM:
        user[USER_CRED]['ig_uname'] = s_uname #hash_uname
        user[USER_CRED]['ig_pwd'] = s_pwd #hash_pwd
    elif s_type == S_TWITTER:
        user[USER_CRED]['twitter_uname'] = s_uname #hash_uname
        user[USER_CRED]['twitter_pwd'] = s_pwd #hash_pwd
    elif s_type == S_LINKEDIN:
        user[USER_CRED]['linkedin_uname'] = s_uname #hash_uname
        user[USER_CRED]['linkedin_pwd'] = s_pwd #hash_pwd

    set_user(uid, user)
    return jsonify(status='succ', 
        source='add_social_integration')

"""
from backend.db_entry import *

def add_social(platform, uid, uname_social, pwd_social):
    user = get_user(uid)
    if user is not None:
        handler = {
            'twitter': set_twitter(uname_social, pwd_social),
            'facebook': set_facebook(uname_social, pwd_social),
            'instagram': set_instagram(uname_social, pwd_social)
        }

        return handler.get(platform, None)
    return None

def set_twitter(user, u, p):
    user['user_credentials']['twitter_uname'] = u
    user['user_credentials']['twitter_pwd'] = p

def set_facebook(user ,u, p):
    user['user_credentials']['fb_uname'] = u
    user['user_credentials']['fb_pwd'] = p

def set_instagram(user ,u, p):
    user['user_credentials']['ig_uname'] = u
    user['user_credentials']['ig_pwd'] = p
"""
