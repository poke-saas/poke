from backend.db_entry import *
from backend.user_auth import *
from backend.internal_utils import *
from scripts.twitter_scraper import *

def check_poke(uid, poke_id):
    user = get_user(uid)
    poke = get_poke(poke_id)

    poke_type = poke['type'][:2]

    handler = {
        'fb': verify_facebook(user, poke),
        'tw': verify_twitter(user, poke),
        'ig': verify_instagram(user, poke)
    }

    return handler.get(poke_type, False)


def verify_twitter(user, poke):
    return check_if_tweet_in_user(poke['data']['body'], user['user_credentials']['twitter_uname'])

def verify_instagram(user, poke):
    return True

def verify_facebook(user, poke):
    return True