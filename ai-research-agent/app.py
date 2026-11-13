from langgraph.graph import StateGraph
from graph.builder import build_graph

def main():
    graph = build_graph()

    question = input("Enter your question: ")

    result = graph.invoke({
        "question": question
    })

    print("\nFinal Answer:\n")
    print(result["answer"])


if __name__ == "__main__":
    main()