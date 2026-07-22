from enum import Enum
from pydantic import BaseModel


class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class Incident(BaseModel):
    id: str
    title: str
    component: str
    test_name: str
    assertion: str
    failure_summary: str
    root_cause: str
    resolution: str
    severity: Severity
    tags: list[str]