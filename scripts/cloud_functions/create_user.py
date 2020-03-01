from backend.db_entry import *
from backend.internal_utils import *
from backend.user_auth import *

def create_new_user(uname, pwd, org_id):
    uid = create_uid(uname, pwd)
    # Create users that are tied to founders
    temp_id, temp_user = new_user_obj()
    temp_user['full_name'] = uname
    temp_user['points'] = 0
    temp_user['org_id'] = org_id
    set_user(uid, temp_user)
    add_org_user(org_id, uid)

