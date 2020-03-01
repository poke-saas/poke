"""
Methods for handling actual application logic
"""
from backend.db_entry import *

# Binary logical checks

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
    user = db.collection(u'Users').document(user_ref).get().to_json()
    poke = db.collection(u'Pokes').document(poke_ref).get().to_json()

    if user is None or poke is None:
        print("User is {} and poke is {}".format(user, poke))
        return False

    return poke['id'] in user['complete_pokes_ids']

def reward_user(user_ref, reward_ref):
    db = get_db()
    user = db.collection(u'Users').document(user_ref).get().to_json()
    reward = db.collection(u'Rewards').document(reward_ref).get().to_json()

    if user is None or reward is None:
        print("User is {} and reward is {}".format(user, reward))
        return

    # Subtract points from the user
    user['points']-=reward['points']
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
    user = db.collection(u'Users').document(user_ref).get().to_json()
    org = db.collection(u'Orgs').document(org_ref).get().to_json()

    if user is None or org is None:
        print("User is {} and org is {}".format(user, org))
        return dict({"error": "user or org is None"})

    if user['id'] not in org['user_ids']:
        print("User is not a member of this organization")
        return dict({"error": "user is not a member of this organization"})

    # If the user is a member of the organization, get all pokes they haven't completed
    result_pokes = dict()
    for poke_id in org['poke_ids']:
        temp_poke = db.collection(u'Pokes').document(poke_id).get().to_json()
        if temp_poke in user['complete_poke_ids']:
            continue
        result_pokes[temp_poke['id']] = result_pokes

    return result_pokes
