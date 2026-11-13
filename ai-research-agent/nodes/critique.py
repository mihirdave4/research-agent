from utils.llm import get_llm

llm = get_llm()

def critique_node(state):
    answer = state["answer"]

    prompt = f"""
    Evaluate this answer:

    {answer}

    If it is incorrect or incomplete, say 'INCORRECT' and explain why.
    Otherwise say 'CORRECT'.
    """

    critique = llm.invoke(prompt)

    return {
        **state,
        "critique": critique
    }