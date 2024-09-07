class ControlAgent:
    def __init__(self, recommendation_agent):
        self.recommendation_agent = recommendation_agent

    def evaluate_success(self):
        query = "SELECT recommendation, reward FROM recommendations"
        cursor = self.recommendation_agent.conn.execute(query)
        success_count = sum([1 for row in cursor if row[1] == 1])
        return f"Total successful actions: {success_count}"

# # Example Usage
# control_Agent = ControlAgent(recommendation_agent)
# print(control_Agent.evaluate_success())
