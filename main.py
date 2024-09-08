# Required Libraries
import os
from agents.DataCollectionAgent import DataCollectionAgent
from agents.SentimentAnalysisAgent import SentimentAnalysisAgent
from agents.TopicAnalysisAgent import TopicAnalysisAgent
from agents.CurrentStateAgent import CurrentStateAgent
from agents.RecommendationAgent import RecommendationAgent
from agents.ControlAgent import ControlAgent



# Human-in-the-loop (Updates rewards manually)
def update_reward_in_table(recommendation_agent, recommendation_id, reward):
    query = "UPDATE recommendations SET reward = ? WHERE id = ?"
    recommendation_agent.conn.execute(query, (reward, recommendation_id))
    recommendation_agent.conn.commit()

# Mocks
process_docs = ["El proceso de compra está conformado por los pasos A, B y C."]

# Initialize Agents
data_agent = DataCollectionAgent()
sentiment_agent = SentimentAnalysisAgent()
topic_agent = TopicAnalysisAgent()
state_agent = CurrentStateAgent(process_docs)
recommendation_agent = RecommendationAgent()
control_manager = ControlAgent(recommendation_agent)

# 1. Data Collection
feedback = data_agent.collect_feedback("Me molesta mucho el proceso de compra, debo pasar por muchos pasos hasta comprar.")
print(f"Collected Feedback: {feedback}")

# 2. Sentiment Analysis
sentiment_label, sentiment_score = sentiment_agent.analyze_sentiment(feedback)
print(f"Sentiment: {sentiment_label}, Score: {sentiment_score}")

# 3. Topic Analysis
topic = topic_agent.extract_topic(feedback)
print(f"Extracted Topic: {topic}")

# 4. Current State Retrieval
# TODO: add RAG, and document processes
current_state = state_agent.get_current_state(topic)
print(f"Current State: {current_state}")

# 5. Actionable Recommendation
action = recommendation_agent.suggest_action(topic, 
                                            feedback,
                                            sentiment_label, 
                                            sentiment_score )
print(f"Suggested Action: {action}")
recommendation_agent.save_recommendation(action, topic)

# 6. Control Manager - Monitoring Improvements
recommendations = recommendation_agent.get_recommendations()
print(f"Current Recommendations in DB: {recommendations}")

# Simulate Human-in-the-loop
update_reward_in_table(recommendation_agent, 1, 1)  # Example: Assigning a positive reward to recommendation ID 1
print(f"Updated Recommendations after Human Feedback: {recommendation_agent.get_recommendations()}")

# Evaluate Success via Control Manager
print(control_manager.evaluate_success())
