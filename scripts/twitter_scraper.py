import tweepy as tw
from scripts.nlp_lib import jaccard_similariy_index, __jaccard_threshold__

__number_of_tweets__ = 10


def scrape_tweets(handle, number_of_tweets):
    """
    Function to scrape tweets based on a user handle
    :param handle: The user's twitter handle
    :param number_of_tweets: The number of tweets we want to get
    :return: (number_of_tweets) tweets from a user
    """
    consumer_key = "t57LC2y3IkCW8xwi6cCvO3wzp"
    consumer_secret = "nI3sK34fuuyB50UFBxty0BKMu2075DtXV8QKwVEpqNHcX0YJSQ"
    access_token_key = "2386644165-wA8wZ6jGFv4OB9Enz9F53ynSrydDXADPy0QAL0X"
    access_token_secret = "SXlOrRpfGJESQvWODV1fMZpzwLn9Pu7BR4vJnQF86dKLz"

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    tweets = list()
    try:
        for tweet in api.user_timeline(id=handle, count=number_of_tweets):
            tweets.append((tweet.created_at, tweet.id, tweet.text))

    except BaseException as e:
        print("failed for some reason: {}".format(e))

    return tweets


def check_if_tweet_in_user(tweet_to_check, handle):
    """
    Checks if a user's recent tweets contains a particular tweet
    :param tweet_to_check: text of the tweet that we're checking
    :param handle: user's handle
    :return: whether or not the user's recent tweets contains that particular text
    """
    user_tweets = scrape_tweets(handle, __number_of_tweets__)

    for tweet in user_tweets:
        if jaccard_similariy_index(tweet_to_check, tweet.text) > __jaccard_threshold__:
            return True
    return False


print(scrape_tweets("dakeenekid", 5))