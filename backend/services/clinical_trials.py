import requests

def fetch_clinical_trials(query: str, max_results: int = 5):
    """
    Fetches clinical trials from ClinicalTrials.gov.
    Using a mock implementation for demonstration.
    """
    print(f"Searching ClinicalTrials for: {query}")
    # Mock data return
    return [
        {"title": f"Clinical Trial for {query} - Phase 1", "status": "Recruiting"},
        {"title": f"Clinical Trial for {query} - Phase 2", "status": "Completed"},
    ]
