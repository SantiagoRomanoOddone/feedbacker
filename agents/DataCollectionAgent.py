from crewai import Agent

class DataCollectionAgent(Agent):
    def __init__(self , role="Data Collection Agent"):
        super().__init__(role=role)
        self.feedback = []

    def collect_feedback(self, feedback):
        self.feedback.append(feedback)
        return feedback
