from agents import DataACollectionAgent, SentimentAnalysisAgent, TopicAnalysisAgent, CurrentStateAgent, RecommendationAgent, ControlAgent

# Initialize Agents
data_agent = DataACollectionAgent()
sentiment_agent = SentimentAnalysisAgent()
topic_agent = TopicAnalysisAgent()
state_agent = CurrentStateAgent()
recommendation_agent = RecommendationAgent()
control_manager = ControlAgent()

# Data Collection
feedback = data_agent.collect_feedback("Me molesta mucho el proceso de compra, debo pasar por muchos pasos hasta comprar.")

# Sentiment Analysis
sentiment_label, sentiment_score = sentiment_agent.analyze_sentiment(feedback)

# Topic Analysis
topic = topic_agent.extract_topic(feedback)

# Current State Analysis
current_state = state_agent.get_current_state(topic)

# Actionable Recommendation
action = recommendation_agent.suggest_action(topic)
recommendation_agent.save_recommendation(action, topic)

# Control Manager monitors progress
print(control_manager.evaluate_success())
