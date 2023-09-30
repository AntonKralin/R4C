from pydantic import BaseModel, Field

from datetime import datetime


class RobotData(BaseModel):
    model: str = Field(min_length=2, max_length=2)
    version: str = Field(min_length=2, max_length=2)
    created: datetime
