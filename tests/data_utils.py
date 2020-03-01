"""
Methods to create testable data.
"""
from backend.internal_utils import *
from backend.db_entry import *
# CONSTANTS


def create_test_data():
    # Create organization for founders
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

    michael_id, michael_user = new_user_obj()
    michael_user['full name'] = "Michael Usachenko"
    michael_user['points'] = 100
    michael_user['org_id'] = org_id
    set_user(michael_id, michael_user)
    add_org_user(org_id, michael_id)

    # Finally, add rewards for the organization
    reward_id, reward_content = new_reward_obj()
    reward_content['cost'] = 25
    reward_content['name'] = "A Patagonia"
    reward_content['desc'] = "Brand new Patagonia jacket!"
    reward_content['img'] = "https://www.bayshoreoutfitters.com/wp-content/uploads/2019/01/Better-Sweater-Jacket_Birch-White.jpg"

    set_reward(reward_id, reward_content)
    add_org_reward(org_id, reward_id)

    # Add pokes to the org
    poke_id, poke_content = new_poke_obj()
    poke_content['cta'] = "tw_tweet"
    poke_content['desc'] = "With 54 coming up, we need YOU to post about it online!"
    poke_content['name'] = "54.io Marketing"
    poke_content['data'] = {"title": poke_content['name'],
                            "body": "Come join Founders at 54 in Fall 2020! #founders #uiuc",
                            "media": None}
    poke_content['pts'] = 50
    set_poke(poke_id, poke_content)
    add_org_poke(org_id, poke_id)

    poke_id_2, poke_content_2 = new_poke_obj()
    poke_content_2['cta'] = "fb_share"
    poke_content_2['desc'] = "Share about Forge on Facebook!"
    poke_content_2['name'] = "Forge Marketing"
    poke_content_2['data'] = dict({"title": poke_content_2['name'],
                            "body": "Don't forget to register for Forge!",
                            "media": None})
    poke_content_2['pts'] = 100
    set_poke(poke_id_2, poke_content_2)
    add_org_poke(org_id, poke_id_2)

create_test_data()