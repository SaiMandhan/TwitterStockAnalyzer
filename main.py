from config import load_config
from auth import authenticate_twitter_app
from fetch_tweets import get_tweets
from sentiment_analysis import analyze_sentiments
import logging

logging.basicConfig(level=logging.INFO)

def main():
    config = load_config()
    api = authenticate_twitter_app(config)
    
    ticker_symbol = "AAPL"
    try:
        tweets = get_tweets(api, ticker_symbol)
        recommendation = analyze_sentiments(tweets)
        print(f"The sentiment for {ticker_symbol} is {recommendation}.")
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()
