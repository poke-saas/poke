### IMPORTS

import os 
import time

import ciso8601
from flask import jsonify
from twilio.rest import Client
from google.cloud import firestore

### CONSTANTS
POKE_FROM_NUM = '+12063124797'
#ACCOUNT_SID = os.environ['ACCOUNT_SID']
ACCOUNT_SID = 'ACfc733d61e38ad54e2838bf65fe379af0'
#AUTH_TOKEN = os.environ['AUTH_TOKEN']
AUTH_TOKEN = '8ccd372fe1be20e13671a9f6a5dec001'

DB = firestore.Client()

REMIND_BODY = "You have Founders pokes due in less than 1 hour! Check the Poke app if you want to redeem points."

def get_all_orgs():
	orgs = DB.collection(u'Orgs').stream()
	return [org.to_dict() for org in orgs]

def get_all_pokes(poke_ids):
	all_pokes = []

	for pid in poke_ids:
		poke = DB.collection(u'Pokes').document(
			pid).get().to_dict()
		all_pokes.append(poke)

	return all_pokes

def get_poke(pid):
	return DB.collection(u'Pokes').document(
		u'{}'.format(pid)).get().to_dict()

def get_all_users(user_ids):
	all_users = []

	for uid in user_ids:
		user = DB.collection(u'Users').document(
			u'{}'.format(uid)).get().to_dict()
		all_users.append(user)

	return all_users

def near_deadline(deadline_str):
	# if current time and deadline are less than 1 hour apart, return true
	ts = ciso8601.parse_datetime(deadline_str)
	ts = time.mktime(ts.timetuple())
	return ts - time.time() < 20000

def send_sms(body, from_num, to_num):
	client = Client(ACCOUNT_SID, AUTH_TOKEN)
	message = client.messages.create(body=body, 
		from_=from_num, to=to_num)

def send_all_possible_reminders():
	orgs = [DB.collection(u'Orgs').document(
		'727bd015fc214a4b').get().to_dict()]

	for o in orgs:
		users = get_all_users(o['user_ids'])
		users = [u for u in users if u is not None]

		for user in users:
			done_pokes = user['complete_pokes_ids']
			diff_pokes = set(o['poke_ids']) - set(done_pokes)

			for p in diff_pokes:
				poke_obj = get_poke(p)

				if near_deadline(poke_obj['deadline']):
					try:
						send_sms(REMIND_BODY, 
							POKE_FROM_NUM, user['phone'])
						break
					except Exception as e:
						print(e)

def entrypoint(requests):
	send_all_possible_reminders()







	




