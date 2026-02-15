from pydantic import BaseModel

class PolicyCreate(BaseModel):
    name: str
    content: str

class PolicyResponse(BaseModel):
    id: int
    name: str
    content: str

    class Config:
        orm_mode = True
