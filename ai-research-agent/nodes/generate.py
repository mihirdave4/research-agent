from utils.llm import get_llm

llm = get_llm()

def generate_node(state):
    question = state["question"]
    docs = state["docs"]

    prompt = f"""
    Use the following information to answer the question.

    {docs}

    Question: {question}
    """

    answer = llm.invoke(prompt)

    return {
        **state,
        "answer": answer
    }