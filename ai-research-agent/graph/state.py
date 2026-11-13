from typing import TypedDict

class GraphState(TypedDict):
    question: str
    docs: str
    answer: str
    critique: str