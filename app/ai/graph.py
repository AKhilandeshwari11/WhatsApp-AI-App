from langgraph.graph import StateGraph, START, END

from .state import AIState
from .nodes import understand_message, generate_reply, format_response


graph_builder = StateGraph(AIState)

graph_builder.add_node("understand", understand_message)
graph_builder.add_node("generate", generate_reply)
graph_builder.add_node("format", format_response)

graph_builder.add_edge(START, "understand")
graph_builder.add_edge("understand", "generate")
graph_builder.add_edge("generate", "format")
graph_builder.add_edge("format", END)

graph = graph_builder.compile()