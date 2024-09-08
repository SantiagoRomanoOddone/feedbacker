from crewai import Agent 

class CurrentStateAgent(Agent):
    def __init__(self, role="Current State Checker", process_docs=None):
        super().__init__(role=role)
        self.process_docs = process_docs if process_docs else ["Default Process Documentation"]
    
    def get_current_state(self, topic):
        for doc in self.process_docs:
            if topic.lower() in doc.lower():
                return doc
        return "No relevant process found."

