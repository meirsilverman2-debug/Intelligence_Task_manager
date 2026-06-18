from pydantic import BaseModel

class Mission(BaseModel):
    title: str
    description: str
    location: str