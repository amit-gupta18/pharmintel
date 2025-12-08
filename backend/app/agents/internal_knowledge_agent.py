from .base_agent import BaseAgent

class InternalKnowledgeAgent(BaseAgent):
    def run(self, query: str):
        return {"source": "Internal DB", "data": f"Internal docs for {query}"}
