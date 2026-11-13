from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

def run_search(query: str) -> str:
    return search.run(query)