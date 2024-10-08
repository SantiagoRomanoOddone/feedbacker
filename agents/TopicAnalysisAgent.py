from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

class TopicAnalysisAgent:
    def __init__(self, n_topics=1):
        self.vectorizer = CountVectorizer()
        self.lda_model = LatentDirichletAllocation(n_components=n_topics, random_state=42)

    def extract_topic(self, feedback):
        matrix = self.vectorizer.fit_transform([feedback])
        self.lda_model.fit(matrix)
        topic = self.lda_model.components_.argmax()
        return self.vectorizer.get_feature_names_out()[topic]

# # Example Usage
# topic_agent = TopicAnalysisAgent()
# topic = topic_agent.extract_topic(feedback)
# print(f"Topic: {topic}")
