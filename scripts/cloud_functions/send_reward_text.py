### IMPORTS
import os 

from twilio.rest import Client
from google.cloud import firestore
from flask import jsonify

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
### CONSTANTS

# US_SMS_CODE = '+1'
POKE_FROM_NUM = '+12063124797'
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']

template_body = 'Poke (Founders): Hi! We are reaching out to confirm you choosing the {} for {} points as your reward! Please reply with a YES or a NO, to confirm or deny.'
DB = firestore.Client()

def get_user(uid):
    return DB.collection(u'Users').document(
        u'{}'.format(uid)).get().to_dict()

def set_user(uid, user_as_json):
    doc_ref = DB.collection(u'Users').document(uid)
    doc_ref.set(user_as_json)

def get_reward(rid):
    return DB.collection(u'Rewards').document(
        rid).get().to_dict()

def format_body(reward_name, reward_points):
	return template_body.format(reward_name, reward_points)

def send_sms(body, from_num, to_num):
	client = Client(ACCOUNT_SID, AUTH_TOKEN)
	message = client.messages.create(body=body, 
		from_=from_num, to=to_num)

def test_entrypoint(uid, rid):
	user_num = get_user(uid)['phone']
	reward = get_reward(rid)
	rname = reward['name']
	rcost = reward['cost']

	body = format_body(rname, rcost)
	send_sms(body, POKE_FROM_NUM, user_num)

def entrypoint(request):
	uid = request.args['uid']
	user_num = get_user(uid)['phone']

	rid = request.args['rid']
	reward = get_reward(rid)
	rname = reward['name']
	rcost = reward['cost']

	body = format_body(rname, rcost)
	send_sms(body, POKE_FROM_NUM, user_num)
	return jsonify(status='success', code='send-reward-text')

"""
if __name__ == '__main__':
	test_entrypoint('1076440981d44efb', '6eb3ec5989704013')
"""


