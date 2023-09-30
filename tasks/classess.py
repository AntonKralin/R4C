from pydantic import BaseModel, Field, EmailStr

from datetime import datetime


class RobotData(BaseModel):
    model: str = Field(min_length=2, max_length=2)
    version: str = Field(min_length=2, max_length=2)
    created: datetime


class OrderData(BaseModel):
    serial: str = Field(min_length=5, max_length=5)
    email: EmailStr
