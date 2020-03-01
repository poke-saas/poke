####################################################
__jaccard_threshold__ = .25


def jaccard_similariy_index(first, second):
    """
    Returns the jaccard similarity between two strings
    :param first: first string we are comparing
    :param second: second string we are comparing
    :return: how similar the two strings are
    """

    # First, split the sentences into words
    tokenize_first = set(first.lower().split())
    tokenize_second = set(second.lower().split())

    # Then, find the ratio between their intersection and their total length
    intersection = tokenize_first.intersection(tokenize_second)
    return float(len(intersection)) / (len(tokenize_first) + len(tokenize_second) - len(intersection))


#############################################################
import json
import uuid
import hashlib
import tweepy as tw
import sys
import os

from igramscraper.instagram import Instagram
from google.cloud import firestore
from flask import jsonify

### CONSTANTS
FIRESTORE_ID = 'export GCLOUD_PROJECT=poke-app-269623'
IG_SESSION_STORE = '/tmp/ig_temp'
USER_ID = None

ORGS_TABLE = u'Orgs'
JC_THRES = __jaccard_threshold__


### TEMP FUNCTIONS
# from .backend.db_entry import get_org, set_user

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

            if jaccard_similariy_index(poke_body, ig_caption) > JC_THRES:
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


##########################################################

### CONSTANTS
FIRESTORE_ID = 'export GCLOUD_PROJECT=poke-app-269623'
DB = firestore.Client()

DUMMY_UUID = '4bec29754ace435f'

USERS_TABLE = u'Users'
DEFAULT_USER = u'user_model'

ORGS_TABLE = u'Orgs'
DEFAULT_ORG = u'orgs_model'

REWARDS_TABLE = u'Rewards'
DEFAULT_REWARD = u'reward_model'

POKES_TABLE = u'Pokes'
DEFAULT_POKE = u'poke_model'

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
def add_claimed_reward(uid, reward_id):
    user = get_user(uid)
    user['complete_pokes_ids'].append(reward_id)
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
    doc_ref.set(org_as_json)


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


def add_org_user(oid, user_ref):
    org = DB.collection(ORGS_TABLE).document(oid).get().to_dict()
    user = DB.collection(USERS_TABLE).document(user_ref).get().to_dict()
    org['user_ids'].append(user['id'])
    set_org(oid, org)


def add_org_poke(oid, poke_id):
    org = get_org(oid)
    org['poke_ids'].append(poke_id)
    set_org(oid, org)


def add_org_reward(oid, reward_id):
    org = get_org(oid)
    org['reward_ids'].append(reward_id)
    set_org(oid, org)


def rm_org_poke(oid, poke_id):
    org = get_org(oid)
    rm_idx = None
    pids = org['poke_ids']

    for idx, p in enumerate(pids):
        if p == poke_id:
            rm_idx = idx
            break

        for idx, pid in enumerate(pids):
            if pid == poke_id:
                rm_idx = idx
                break

    if rm_idx is not None:
        pids.pop(rm_idx)
    else:
        pass
    # todo handle errors

    org['poke_ids'] = pids
    set_org(oid, org)


def rm_org_reward(oid, reward_id):
    org = get_org(oid)
    rm_idx = None
    rids = org['reward_ids']

    for idx, rid in enumerate(rids):
        if rid == reward_id:
            rm_idx = idx
            break

    if rm_idx is not None:
        rids.pop(rm_idx)
    else:
        pass
    # todo handle errors

    org['reward_ids'] = rids
    set_org(oid, org)


def rm_org_reward():
    pass


### POKE HELPER METHODS
def get_poke_template():
    template = DB.collection(POKES_TABLE).document(DEFAULT_POKE).get().to_dict()

    template['cta'] = str()
    template['data'] = dict()
    template['desc'] = str()
    template['name'] = str()
    template['points'] = 0

    return template


def new_poke_obj():
    new_pid = uuid.uuid4().hex[:16]
    new_poke = get_poke_template()
    new_poke['id'] = new_pid
    return new_pid, new_poke


def get_poke(pid):
    return DB.collection(POKES_TABLE).document(
        u'{}'.format(pid)).get().to_dict()


def set_poke(pid, poke_as_json):
    doc_ref = DB.collection(POKES_TABLE).document(pid)
    doc_ref.set(poke_as_json)


def add_new_poke():
    new_pid, new_poke = new_poke_obj()
    set_poke(new_pid, new_poke)
    return new_pid


def rm_poke(pid):
    DB.collection(POKES_TABLE).document(pid).delete()


### REWARD HELPER METHODS
def get_reward_template():
    return DB.collection(REWARDS_TABLE).document(
        DEFAULT_REWARD).get().to_dict()


def new_reward_obj():
    new_rid = uuid.uuid4().hex[:16]
    new_reward = get_reward_template()
    new_reward['id'] = new_rid
    return new_rid, new_reward


def get_reward(rid):
    return DB.collection(REWARDS_TABLE).document(
        rid).get().to_dict()


def set_reward(rid, reward_as_json):
    doc_ref = DB.collection(REWARDS_TABLE).document(rid)
    doc_ref.set(reward_as_json)


def add_reward(name, desc, cost, img_link):
    new_rid, new_reward = new_reward_obj()
    new_reward['name'] = name
    new_reward['desc'] = desc
    new_reward['cost'] = cost
    new_reward['img'] = img_link
    set_reward(new_rid, new_reward)


def rm_reward(rid):
    DB.collection(REWARDS_TABLE).document(rid).delete()


def get_all_elements():
    db = DB
    all_fields = dict()

    all_org_info = db.collection(u'Orgs')
    orgs = all_org_info.stream()

    for org in orgs:
        all_fields[org.id] = org.to_dict()

    return all_fields


###########################################################3
__number_of_tweets__ = 10


def scrape_tweets(handle, number_of_tweets):
    """
    Function to scrape tweets based on a user handle
    :param handle: The user's twitter handle
    :param number_of_tweets: The number of tweets we want to get
    :return: (number_of_tweets) tweets from a user
    """
    consumer_key = "bDTIoK0pn0gX7oniVhnI1ewnU"
    consumer_secret = "KaHGOEkkUculbGAWOJ8KDSRxRH1GU4ZpLLuRRrlQFoasDa0msm"
    access_token_key = "2386644165-wA8wZ6jGFv4OB9Enz9F53ynSrydDXADPy0QAL0X"
    access_token_secret = "SXlOrRpfGJESQvWODV1fMZpzwLn9Pu7BR4vJnQF86dKLz"

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    tweets = list()
    try:
        for tweet in api.home_timeline(id=handle, count=number_of_tweets):
            timestamp = tweet.created_at
            id = tweet.id
            text = tweet.text
            media = tweet.entities.get('media', [])
            if (len(media) > 0):
                media = media[0]['media_url']
            tweets.append({
                "timestamp": timestamp,
                "id": id,
                "text": text,
                "media": media
            })

    except BaseException as e:
        print("failed for some reason: {}".format(e))

    return tweets


def check_if_tweet_in_user(tweet_to_check, handle):
    """
    Checks if a user's recent tweets contains a particular tweet
    :param tweet_to_check: text of the tweet that we're checking
    :param handle: user's handle
    :return: whether or not the user's recent tweets contains that particular text
    """
    user_tweets = scrape_tweets(handle, __number_of_tweets__)

    for tweet in user_tweets:
        if jaccard_similariy_index(tweet_to_check, tweet['text']) > __jaccard_threshold__:
            return True
    return False


def check_single_poke(user, poke_id):
    poke = get_poke(poke_id)
    if (check_if_tweet_in_user(poke['data']['body'], user['user_credentials']['twitter_uname'])):
        return poke['pts']
    return None


#########################################################

def check_poke(uid, poke_id):
    user = get_user(uid)
    poke = get_poke(poke_id)

    poke_type = poke['cta'][:2]

    handler = {
        'fb': verify_facebook(user, poke),
        'tw': verify_twitter(user, poke),
        'ig': verify_instagram(user, poke)
    }

    return handler.get(poke_type, False)


def verify_twitter(user, poke):
    if (check_if_tweet_in_user(poke['data']['body'], user['user_credentials']['twitter_uname'])):
        return poke['pts']
    return None


def verify_instagram(user, poke):
    return check_single_poke(user, poke['id'])


def verify_facebook(user, poke):
    return True


#########################################################
def can_user_claim_reward(user_ref, reward_ref):
    db = get_db()
    user = db.collection(u'Users').document(user_ref).get().to_dict()
    reward = db.collection(u'Rewards').document(reward_ref).get().to_dict()

    if user is None or reward is None:
        print("User is {} and reward is {}".format(user, reward))
        return False

    return user['points'] <= reward['cost']


def did_user_complete_poke(user_ref, poke_ref):
    db = get_db()
    user = db.collection(u'Users').document(user_ref).get().to_dict()
    poke = db.collection(u'Pokes').document(poke_ref).get().to_dict()

    if user is None or poke is None:
        print("User is {} and poke is {}".format(user, poke))
        return False

    return poke['id'] in user['complete_pokes_ids']


def reward_user(user_ref, reward_ref):
    db = get_db()
    user = db.collection(u'Users').document(user_ref).get().to_dict()
    reward = db.collection(u'Rewards').document(reward_ref).get().to_dict()

    if user is None or reward is None:
        print("User is {} and reward is {}".format(user, reward))
        return

    # Subtract points from the user
    user['points'] -= reward['points']
    # Add reward to their claimed rewards
    user['claimed_reward_ids'].append(reward['id'])
    # Update database
    set_user(user['uid'], user)


def get_unfinished_pokes(user_ref, org_ref):
    """
    Gets the unfinished pokes for a particular user, given that they're in an organization
    :param user_ref: User who we are getting pokes for
    :param org_ref: Organization of pokes
    :return: json array of unfinished pokes
    """
    db = get_db()
    user = db.collection(u'Users').document(user_ref).get().to_dict()
    org = db.collection(u'Orgs').document(org_ref).get().to_dict()

    if user is None or org is None:
        print("User is {} and org is {}".format(user, org))
        return dict({"error": "user or org is None"})

    if user['id'] not in org['user_ids']:
        print("User is not a member of this organization")
        return dict({"error": "user is not a member of this organization"})

    # If the user is a member of the organization, get all pokes they haven't completed
    result_pokes = dict()
    for poke_id in org['poke_ids']:
        temp_poke = db.collection(u'Pokes').document(poke_id).get().to_dict()
        if temp_poke['id'] in user['complete_pokes_ids']:
            continue
        else:
            result_pokes[temp_poke['id']] = temp_poke

    return result_pokes


################################################################3
def create_uid(uname, pwd):
    hash_input = "{}{}".format(uname, pwd).encode('utf-8')
    hash_output = hashlib.md5(hash_input).hexdigest()
    return hash_output


def verify_uid(hash, uname, pwd):
    return hash == hashlib.md5("{}{}".format(uname, pwd).encode('utf-8')).hexdigest()


def login_internal(uname, pwd):
    """
    Returns the user if exists, otherwise None
    :param uname: username of user
    :param pwd: password
    :return: user object of the credentials
    """
    uid = create_uid(uname, pwd)
    user = get_user(uid)
    if user is None:
        print("Username or password is invalid!")
    return user


def create_new_user(uname, pwd, org_id):
    uid = create_uid(uname, pwd)
    # Create users that are tied to founders
    temp_id, temp_user = new_user_obj()
    temp_user['full_name'] = uname
    temp_user['points'] = 0
    temp_user['org_id'] = org_id
    set_user(uid, temp_user)
    add_org_user(org_id, uid)
    return uid, temp_user


##############################################################
def main(request):
    arg = request.args['function']
    try:
        if arg == 'check_poke':
            points = check_poke(request.args['uid'],
                                request.args['poke_id'])

            if points is not None:
                return jsonify(message="Poke is verified!",
                               points=points,
                               uid=request.args['uid'],
                               poke_id=request.args['poke_id'])
            else:
                return jsonify(message="Poke is not verified!",
                               points=points,
                               uid=request.args['uid'],
                               poke_id=request.args['poke_id'])
        if arg == 'poke_refresh':
            uid = request.args['uid']
            user = get_user(uid)
            org_id = user['org_id']
            pokes = get_unfinished_pokes(uid, org_id)
            return jsonify(pokes=pokes,
                           message="success!")
        if arg == 'create_user':
            uname = request.args['uname']
            pwd = request.args['pwd']
            org_id = request.args['org_id']
            uid, user = create_new_user(uname, pwd, org_id)
            return jsonify(uid=uid,
                           user=user,
                           message="success!")
        if arg == 'login':
            uname = request.args['uname']
            pwd = request.args['pwd']
            user = login_internal(uname, pwd)
            return jsonify(user=user,
                           message="success!")

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        return jsonify(exc_type=exc_type, exc_obj=exc_obj, exc_tb=exc_tb, fname=fname, message="error!")