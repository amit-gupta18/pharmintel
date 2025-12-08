from .base_agent import BaseAgent

class ClinicalAgent(BaseAgent):
    def run(self, query: str):
        return {"source": "ClinicalTrials.gov", "data": f"Trial data for {query}"}
