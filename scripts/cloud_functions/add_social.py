from backend.db_entry import *

def add_social(platform, uid, uname_social, pwd_social):
    user = get_user(uid)
    if user is not None:
        handler = {
            'twitter': set_twitter(uname_social, pwd_social),
            'facebook': set_facebook(uname_social, pwd_social),
            'instagram': set_instagram(uname_social, pwd_social)
        }

        return handler.get(platform, None)
    return None

def set_twitter(user, u, p):
    user['user_credentials']['twitter_uname'] = u
    user['user_credentials']['twitter_pwd'] = p

def set_facebook(user ,u, p):
    user['user_credentials']['fb_uname'] = u
    user['user_credentials']['fb_pwd'] = p

def set_instagram(user ,u, p):
    user['user_credentials']['ig_uname'] = u
    user['user_credentials']['ig_pwd'] = p