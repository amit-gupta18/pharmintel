from .base_agent import BaseAgent

class EXIMAgent(BaseAgent):
    def run(self, query: str):
        return {"source": "EXIM", "data": f"Import/Export data for {query}"}
