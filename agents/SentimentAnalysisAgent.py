from transformers import pipeline

class SentimentAnalysisAgent:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")

    def analyze_sentiment(self, text):
        sentiment = self.model(text)[0]
        return sentiment['label'], sentiment['score']

# # Example Usage
# sentiment_agent = SentimentAnalysisAgent()
# sentiment_label, sentiment_score = sentiment_agent.analyze_sentiment(feedback)
# print(f"Sentiment: {sentiment_label}, Score: {sentiment_score}")