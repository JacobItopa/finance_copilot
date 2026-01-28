from pydantic import BaseModel
from typing import Literal


class Recommendation(BaseModel):
    priority: Literal["critical", "important", "info"]
    title: str
    action: str
    rationale: str
