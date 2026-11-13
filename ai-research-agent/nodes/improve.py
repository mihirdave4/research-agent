from utils.llm import get_llm

llm = get_llm()

def improve_node(state):
    answer = state["answer"]
    critique = state["critique"]

    prompt = f"""
    Improve the answer:

    Original Answer:
    {answer}

    Critique:
    {critique}
    """

    improved = llm.invoke(prompt)

    return {
        **state,
        "answer": improved
    }