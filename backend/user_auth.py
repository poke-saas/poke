from backend.db_entry import *

import hashlib

"""
Authentication lib
"""

def create_uid(uname, pwd):
    hash_input = "{}{}".format(uname, pwd).encode('utf-8')
    hash_output = hashlib.md5(hash_input).hexdigest()
    return hash_output

def verify_uid(hash, uname, pwd):
    return hash == hashlib.md5("{}{}".format(uname, pwd).encode('utf-8')).hexdigest()

def login_internal(uname, pwd):
    """
    Returns the user if exists, otherwise None
    :param uname: username of user
    :param pwd: password
    :return: user object of the credentials
    """
    uid = create_uid(uname, pwd)
    user = get_user(uid)
    if user is None:
        print("Username or password is invalid!")
    return user


if __name__ == '__main__':
    print(create_uid("davis", "password"))
    print(verify_uid(create_uid("davis", "password"), "davis", "password"))