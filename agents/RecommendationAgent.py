import sqlite3
from crewai import Agent

class RecommendationAgent(Agent):
    def __init__(self, db_name="recommendations.db"):
        super().__init__(role="Action Recommender")
        self.conn = sqlite3.connect(db_name)
        self.create_table()
    
    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS recommendations (
                        id INTEGER PRIMARY KEY,
                        recommendation TEXT,
                        topic TEXT,
                        reward INTEGER
                    )"""
        self.conn.execute(query)

    def suggest_action(self, 
                       topic, 
                       feedback=None,
                        sentiment_label=None, 
                        sentiment_score=None):
        # TODO: add LLM here
        actions = {
            "compra": "Reducir los pasos hasta compra.",
        }
        action = actions.get(topic, "No suggestion available.")
        return action

    def save_recommendation(self, recommendation, topic, reward=None):
        query = "INSERT INTO recommendations (recommendation, topic, reward) VALUES (?, ?, ?)"
        self.conn.execute(query, (recommendation, topic, reward))
        self.conn.commit()

    def get_recommendations(self):
        query = "SELECT * FROM recommendations"
        cursor = self.conn.execute(query)
        return cursor.fetchall()


