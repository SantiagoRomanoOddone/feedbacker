
class DataCollectionAgent:
    def __init__(self):
        self.feedback = []

    def collect_feedback(self, feedback):
        self.feedback.append(feedback)
        return feedback

# # Example Usage
# data_agent = DataCollectionAgent()
# feedback = data_agent.collect_feedback("Me molesta mucho el proceso de compra, debo pasar por muchos pasos hasta comprar.")
