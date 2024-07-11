import tweepy
import datetime
import logging

logging.basicConfig(level=logging.INFO)

def get_tweets(api, ticker_symbol):
    tweets = []
    today = datetime.datetime.utcnow().date()

    try:
        for tweet in tweepy.Cursor(api.search_tweets, q=f"${ticker_symbol} -filter:retweets", lang="en", tweet_mode='extended').items(1000):
            if (today - tweet.created_at.date()).days <= 7:
                tweets.append(tweet.full_text)
        logging.info(f"Fetched {len(tweets)} tweets for the ticker: {ticker_symbol}")
    except Exception as e:
        logging.error(f"Failed to fetch tweets: {str(e)}")
    return tweets
