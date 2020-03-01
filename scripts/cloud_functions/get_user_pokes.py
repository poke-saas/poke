from scripts.db_utils import *
from backend.internal_utils import *

def get_user_unfinished_pokes(request):
    uid = request.args['uid']
    user = get_user(uid)
    org_id = user['org_id']
    return get_unfinished_pokes(uid, org_id)