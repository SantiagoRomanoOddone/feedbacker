from transformers import pipeline
from crewai import Agent

class SentimentAnalysisAgent(Agent):
    def __init__(self, role="Sentiment Analyzer"):
        super().__init__(role=role)
        self.model = pipeline("sentiment-analysis")
    
    def analyze_sentiment(self, feedback):
        result = self.model(feedback)[0]
        return {"sentiment": result['label'], "score": result['score']}


