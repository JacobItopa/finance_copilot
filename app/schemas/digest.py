from pydantic import BaseModel
from typing import List


class DailyDigest(BaseModel):
    date: str
    summary: str
    key_metrics: dict
    alerts: List[str]
    recommendations: List[str]
