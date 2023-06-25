import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('vader_lexicon')

def perform_sentiment_analysis(sentence):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    
    # Perform sentiment analysis using VADER
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(sentence)
    
    # Determine if the text is offensive based on the sentiment scores
    is_offensive = sentiment_scores['compound'] < 0
    
    # Return the sentiment analysis result
    if is_offensive:
        return "offensive"
    else:
        return "not offensive"

# Example usage
sentence = "heidrun absolutely problem designated toilet male female chose toilet based gender want identify fairytale world"
result = perform_sentiment_analysis(sentence)
print("Sentiment: " + result)
