### IMPORTS

import os
import json

import requests
from flask import jsonify

### HELPER FUNCTIONS

def generate_fb_oauth_url(code_from_req):
    base_url = 'https://graph.facebook.com/v6.0/oauth/access_token'

    client_id = "client_id={}".format(
        os.environ['FB_APP_ID'])

    client_secret = "client_secret={}".format(
        os.environ['FB_APP_SECRET'])

    redir_uri = "redirect_uri={}".format(
        os.environ['REDIR_URI'])

    code = "code={}".format(code_from_req)

    full_url = "{}?{}&{}&{}&{}"

    return full_url.format(
        base_url, client_id, client_secret, redir_uri, code)

### ENTRYPOINT

def get_auth_key_for_user(request):

    oauth_token = request.args['code']
    auth_rq = None

    # set up auth url + get access token
    try:
        fb_auth_url = generate_fb_oauth_url(oauth_token)
        auth_rq = requests.get(fb_auth_url).json()
    except Exception as e:
        return jsonify(error=str(e), 
            auth_rq=auth_rq['access_token'])




