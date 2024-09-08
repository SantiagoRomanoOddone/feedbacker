from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from crewai import Agent

class TopicAnalysisAgent(Agent):
    def __init__(self, role="Topic Analyzer"):
        super().__init__(role=role)
        self.vectorizer = CountVectorizer()
        self.lda_model = LatentDirichletAllocation(n_components=1, random_state=42)

    def extract_topic(self, feedback):
        matrix = self.vectorizer.fit_transform([feedback])
        self.lda_model.fit(matrix)
        topic = self.lda_model.components_.argmax()
        return self.vectorizer.get_feature_names_out()[topic]

