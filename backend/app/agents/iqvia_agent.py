from .base_agent import BaseAgent

class IQVIAAgent(BaseAgent):
    def run(self, query: str):
        return {"source": "IQVIA", "data": f"Market data for {query}"}
