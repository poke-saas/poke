from backend.db_entry import *

def get_rewards(uid):
    user = get_user(uid)
    org_id = user['org_id']
