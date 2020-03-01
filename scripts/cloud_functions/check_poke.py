from scripts.twitter_scraper import check_if_tweet_in_user
from scripts.instagram_scraper import *
from backend.db_entry import *

def check_poke(uid, poke_id):
    user = get_user(uid)
    poke = get_poke(poke_id)

    poke_type = poke['cta'][:2]

    handler = {
        'fb': verify_facebook(user, poke),
        'tw': verify_twitter(user, poke),
        'ig': verify_instagram(user, poke)
    }

    return handler.get(poke_type, False)

def verify_twitter(user, poke):
    if(check_if_tweet_in_user(poke['data']['body'], user['user_credentials']['twitter_uname'])):
        return poke['pts']
    return None

def verify_instagram(user, poke):
    return check_single_poke(user, poke['id'])

def verify_facebook(user, poke):
    return True