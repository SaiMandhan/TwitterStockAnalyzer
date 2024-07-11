from textblob import TextBlob
import logging

logging.basicConfig(level=logging.INFO)

def analyze_sentiments(tweets):
    if not tweets:
        logging.info("No tweets to analyze.")
        return "No sufficient data for analysis."

    sentiment_scores = [TextBlob(tweet).sentiment.polarity for tweet in tweets]
    average_score = sum(sentiment_scores) / len(sentiment_scores)
    logging.info(f"Calculated average sentiment score: {average_score}")

    if average_score > 0.05:
        return "Bullish"
    elif average_score < -0.05:
        return "Bearish"
    else:
        return "Neutral"
