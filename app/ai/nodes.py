import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from .state import AIState

load_dotenv()


def understand_message(state: AIState) -> AIState:
    message = state["message"].lower()

    if any(word in message for word in ["price", "cost", "how much"]):
        intent = "pricing"
    elif any(word in message for word in ["hello", "hi", "hey"]):
        intent = "greeting"
    elif any(word in message for word in ["help", "support", "problem"]):
        intent = "support"
    else:
        intent = "general"

    state["intent"] = intent
    return state


def generate_reply(state: AIState) -> AIState:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        state["response"] = "AI API key is not configured yet."
        return state

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        api_key=api_key,
    )

    prompt = f"""
You are a helpful WhatsApp customer support assistant.

Customer message:
{state["message"]}

Detected intent:
{state["intent"]}

Generate a short, friendly and professional reply.
"""

    result = llm.invoke(prompt)

    state["response"] = result.content

    return state
def format_response(state: AIState) -> AIState:
    response = state["response"].strip()

    state["response"] = response

    return state