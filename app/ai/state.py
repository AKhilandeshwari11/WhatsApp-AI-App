from typing import TypedDict, List


class AIState(TypedDict):
    phone: str
    message: str
    intent: str
    response: str
    history: List[str]