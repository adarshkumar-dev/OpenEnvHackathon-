from pydantic import BaseModel
from typing import List, Optional, Literal, Dict

class Observation(BaseModel):
    ticket_id: str
    customer_message: str
    customer_history: List[str]
    priority: Literal["low", "medium", "high"]
    category_hint: Optional[str]
    time_elapsed: int

class Action(BaseModel):
    action_type: Literal[
        "classify_ticket",
        "reply_to_customer",
        "escalate_ticket",
        "request_more_info",
        "close_ticket"
    ]
    content: Optional[str]

class Reward(BaseModel):
    score: float
    breakdown: Dict[str, float]
