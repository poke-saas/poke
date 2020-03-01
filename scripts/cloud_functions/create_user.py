from backend.db_entry import *
from backend.internal_utils import *
from backend.user_auth import *

def create_new_user(uname, pwd, org_id):
    org_id, new_org = new_org_obj()
    new_org['name'] = "Founders"
    set_org(org_id, new_org)

    # Create users that are tied to founders
    siraj_id, siraj_user = new_user_obj()
    siraj_user['full_name'] = "Siraj Chokshi"
    siraj_user['points'] = 100
    siraj_user['org_id'] = org_id
    set_user(siraj_id, siraj_user)
    add_org_user(org_id, siraj_id)