from .base_agent import BaseAgent

class PatentAgent(BaseAgent):
    def run(self, query: str):
        return {"source": "USPTO", "data": f"Patent data for {query}"}
