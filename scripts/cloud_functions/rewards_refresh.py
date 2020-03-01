
from google.cloud import firestore
from flask import jsonify
DB = firestore.Client()

def get_org(oid):
    return DB.collection(u'Orgs').document(
        u'{}'.format(oid)).get().to_dict()

def get_user(uid):
    return DB.collection(u'Users').document(
        u'{}'.format(uid)).get().to_dict()

def get_reward(rid):
    return DB.collection(u'Rewards').document(
        rid).get().to_dict()

def get_rewards_entrypoint(request):
	uid = request.args['uid']
	org_id = get_user(uid)['org_id']
	rewards_json = []

	for r in get_org(org_id)['reward_ids']: 
		rewards_json.append(get_reward(r))

	return jsonify(rewards=rewards_json)

