from services.pubmed import fetch_pubmed_articles
from services.clinical_trials import fetch_clinical_trials

class MasterAgent:
    def __init__(self):
        pass

    def run(self, query: str):
        print(f"MasterAgent retrieving data for: {query}")
        
        pubmed_data = fetch_pubmed_articles(query)
        clinical_data = fetch_clinical_trials(query)
        
        # In a real scenario, an LLM would synthesize this data.
        return {
            "query": query,
            "pubmed_results": pubmed_data,
            "clinical_trials_results": clinical_data,
            "synthesis": f"Found {len(pubmed_data)} articles and {len(clinical_data)} trials directly related to {query}."
        }

master_agent = MasterAgent()
