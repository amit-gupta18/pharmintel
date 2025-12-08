from .base_agent import BaseAgent

class WebIntelAgent(BaseAgent):
    def run(self, query: str):
        return {"source": "Web", "data": f"Web search results for {query}"}
