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

    # Create users that are tied to founders
    siraj_id, siraj_user = new_user_obj()
    siraj_user['full_name'] = "Siraj Chokshi"
    add_social_integration(siraj_id, 0, "sirajchokshi@gmail.com", "exampl3")
    siraj_user['points'] = 100
    add_org_user(org_id, siraj_user)

    michael_id, michael_user = new_user_obj()
    michael_user['full name'] = "Michael Usachenko"
    add_social_integration(michael_id, 1, "themichaelusa@example.com", "passwd")
    michael_user['points'] = 100
    add_org_user(org_id, michael_user)


    # Add pokes to the org
    poke_id, poke_content = new_poke_obj()
    poke_content['cta'] = "tw_tweet"
    poke_content['desc'] = "With 54 coming up, we need YOU to post about it online!"
    poke_content['name'] = "54.io Marketing"
    poke_content['data'] = {"title": poke_content['name'],
                            "body": "Come join Founders at 54 in Fall 2020! #founders #uiuc",
                            "media": None}
    poke_content['pts'] = 50
    add_org_poke(org_id, poke_content)

    poke_id_2, poke_content_2 = new_poke_obj()
    poke_content['cta'] = "fb_share"
    poke_content['desc'] = "Share about Forge on Facebook!"
    poke_content['name'] = "Forge Marketing"
    poke_content['data'] = {"title": poke_content_2['name'],
                            "body": "Don't forget to register for Forge!",
                            "media": None}
    poke_content['pts'] = 100
    add_org_poke(org_id, poke_content_2)


create_test_data()