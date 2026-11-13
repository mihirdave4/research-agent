from langgraph.graph import StateGraph, END

from graph.state import GraphState
from nodes.search import search_node
from nodes.generate import generate_node
from nodes.critique import critique_node
from nodes.improve import improve_node


def should_improve(state):
    if "INCORRECT" in state["critique"]:
        return "improve"
    return "end"


def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("search", search_node)
    builder.add_node("generate", generate_node)
    builder.add_node("critique", critique_node)
    builder.add_node("improve", improve_node)

    builder.set_entry_point("search")

    builder.add_edge("search", "generate")
    builder.add_edge("generate", "critique")

    builder.add_conditional_edges(
        "critique",
        should_improve,
        {
            "improve": "improve",
            "end": END
        }
    )

    builder.add_edge("improve", "critique")

    return builder.compile()   