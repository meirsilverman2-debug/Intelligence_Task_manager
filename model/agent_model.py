from pydantic import BaseModel

class Agent(BaseModel):
    name: str
    specialty: str
    agent_rank: str = None