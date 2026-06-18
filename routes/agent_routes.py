from fastapi import APIRouter
from database.agent_db import agentdb
from model.agent_model import Agent
from logs.logger_config import logger

agentdb.get_agent_performance


router = APIRouter(prefix="/agentes", tags=["agentes"])

@router.post("/gents")
def create_agent(data: Agent):
    logger.info("post/agent call")
    return agentdb.create_agent(data)


@router.get("/gents")
def get_all_agents():
    logger.info("get/agent call")
    return agentdb.get_all_agents()


@router.get("/agents/{id}")
def get_agent_by_id(id: int):
    logger.info("get/agents/{id} call")
    return agentdb.get_agent_by_id(id)


@router.put("/agents/{id}")
def update_agent(id: int, data: Agent):
    logger.info("put/agents/{id} call")
    return agentdb.update_agent(id, data)


@router.put("/agents/{id}/deactivate")
def deactivate_id(id: int):
    logger.info("put/agent/{id}/deactivate call")
    return agentdb.deactivate_id(id) 


@router.get("/agents/{id}/performance")
def get_agent_performance(id: int):
    logger.info("get/agent/{id}/performance call")
    return agentdb.get_agent_performance(id)