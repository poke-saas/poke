from requests_oauthlib import OAuth1Session
import requests
import os
from flask import jsonify
import webbrowser

consumer_key = "bDTIoK0pn0gX7oniVhnI1ewnU"
consumer_secret = "KaHGOEkkUculbGAWOJ8KDSRxRH1GU4ZpLLuRRrlQFoasDa0msm"

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'

def get_access_token(consumer_key, consumer_secret):
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret)
    try:
        resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)
    except ValueError as e:
        print
        'Invalid respond from Twitter requesting temp token: %s' % e
        return jsonify(error=str(e),
                       message="invalid response from twitter requesting temp token")

    url = oauth_client.authorization_url(AUTHORIZATION_URL)
    webbrowser.open(url)

    verifier=input("pin? ")

    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret,
                                 resource_owner_key=resp.get('oauth_token'),
                                 resource_owner_secret=resp.get('oauth_token_secret'),
                                 verifier=verifier
                                 )

    try:
        resp = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
    except ValueError as e:
        print
        'Invalid respond from Twitter requesting access token: %s' % e
        return jsonify(error=str(e),
                       message="invalid response requesting access token")

    return [resp.get('oauth_token'), resp.get('oauth_token_secret')]


def get_resource_token():
    #create an object of OAuth1Session
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret)
    try:
        resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)
    except ValueError as e:
        print
        'Invalid respond from Twitter requesting temp token: %s' % e
        return jsonify(error=str(e),
                       message="invalid response from twitter requesting temp token")
    print(oauth_client.authorization_url(AUTHORIZATION_URL))
    return [resp.get('oauth_token'), resp.get('oauth_token_secret')]

def twitter_get_access_token(verifier, ro_key, ro_secret):
    oauth_token = OAuth1Session(client_key=consumer_key,
                                client_secret=consumer_secret,
                                resource_owner_key=ro_key,
                                resource_owner_secret=ro_secret,
                                verifier=verifier)
    url2 = "https://api.twitter.com/oauth/access_token"
    data = {'oauth_verifier': verifier}
    access_token_data = oauth_token.post(url2, data=data)
    access_token_list = str.split(access_token_data.text, '&')
    return access_token_list


def twitter_get_user_data(access_token_list):
    access_token_key = str.split(access_token_list[0], '=')
    access_token_secret = str.split(access_token_list[1], '=')
    access_token_name = str.split(access_token_list[3], '=')
    access_token_id = str.split(access_token_list[2], '=')
    key = access_token_key[1]
    secret = access_token_secret[1]
    name = access_token_name[1]
    id = access_token_id[1]
    oauth_user = OAuth1Session(client_key=consumer_key,
                               client_secret=consumer_secret,
                               resource_owner_key=key,
                               resource_owner_secret=secret)
    url_user = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    params = {"include_email": 'true'}
    user_data = oauth_user.get(url_user, params=params)

    return user_data.json()

# Testing
def main(request):
    request_token_key = get_resource_token()
    print(request)
    verifier = request.split("oauth_verifier=")[1]
    print(verifier)
    try:
        access_token_list = twitter_get_access_token(verifier, request_token_key[0], request_token_key[1])
        user_data = twitter_get_user_data(access_token_list)
        print(user_data)

    except Exception as e:
        print("exception occured")

rt = get_resource_token()