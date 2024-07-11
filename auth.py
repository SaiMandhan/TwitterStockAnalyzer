import tweepy
import logging

logging.basicConfig(level=logging.INFO)

def authenticate_twitter_app(config):
    auth = tweepy.OAuthHandler(config['API_KEYS']['CONSUMER_KEY'], config['API_KEYS']['CONSUMER_SECRET'])
    auth.set_access_token(config['API_KEYS']['ACCESS_TOKEN'], config['API_KEYS']['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    logging.info("Authenticated with Twitter API successfully.")
    return api
