from tools.search_tool import run_search

def search_node(state):
    query = state["question"]
    results = run_search(query)
    
    return {
        **state,
        "docs": results
    }