from sqlmodel import SQLModel, Field
from pydantic import BaseModel, EmailStr

class CallDataExtract(BaseModel):
    client_name: str
    phone_number: str
    call_purpose: str
    status: str = "pendiente"

class CallSession(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    client_name: str
    phone_number: str
    call_purpose: str
    status: str