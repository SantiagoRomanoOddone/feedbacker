class CurrentStateAgent:
    def __init__(self, process_docs):
        self.process_docs = process_docs

    def get_current_state(self, topic):
        # In reality, you would implement retrieval of relevant process documents
        for doc in self.process_docs:
            if topic.lower() in doc.lower():
                return doc
        return "No matching process found."

# # Example Usage
# process_docs = ["El proceso de compra está conformado por los pasos A, B y C."]
# state_agent = CurrentStateAgent(process_docs)
# current_state = state_agent.get_current_state(topic)
# print(f"Current State: {current_state}")
