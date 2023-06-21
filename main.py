import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def perform_sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    # Interpret the sentiment scores
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Example usage
input_text = "I love this movie! It's so amazing."
sentiment = perform_sentiment_analysis(input_text)
print(f"Sentiment: {sentiment}")
