import requests

def fetch_pubmed_articles(query: str, max_results: int = 5):
    """
    Fetches articles from PubMed based on a query.
    Note: Ideally use Biopython or handle rate limits/API keys properly.
    For this demo, we'll use a public search URL or a mock if API access is restricted.
    Here we use a mock implementation for demonstration as no API key was provided.
    """
    print(f"Searching PubMed for: {query}")
    # Mock data return
    return [
        {"title": f"Study on {query} - A", "summary": "Detailed summary of study A..."},
        {"title": f"Study on {query} - B", "summary": "Detailed summary of study B..."},
    ]
