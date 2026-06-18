from fastapi import APIRouter, HTTPException
from database.mission_db import missiondb
from model.mission_model import Mission
from logs.logger_config import logger

router = APIRouter(prefix="/missions", tags=["missions"])


@router.post("/missions")
def creat_mission(data: Mission):
    logger.info("post/missions call")
    return missiondb.creat_mission(data)


@router.get("/missions")
def get_all_missions():
    logger.info("get/missions call")
    return missiondb.get_all_missions()


@router.get("/missions/{id}")
def get_mission_by_id(id: int):
    logger.info("get/missions/{id} call")
    return missiondb.get_mission_by_id(id)


@router.put("/missions/{id}/assign/{agent_id}")
def assign_mission(id: int, agent_id: int):
    logger.info("put/missions/{id}/assign/{agent_id} call")
    return missiondb.assign_mission(id, agent_id)


@router.put("/missions/{id}/start")
def update_mission_status(id: int):
    logger.info("put/missions/{id}/start call")
    status = "in_progress"
    missiondb.update_mission_status(id, status)


@router.put("/missions/{id}/complete")
def update_mission_status():
    logger.info("put/missions/{id}/complete call")
    status = "completed"
    missiondb.update_mission_status(id, status)


@router.put("/missions/{id}/fail")
def update_mission_status():
    logger.info("put/missions/{id}/fail call")
    status = "failed"
    missiondb.update_mission_status(id, status)


@router.put("/missions/{id}/cancel")
def update_mission_status():
    logger.info("put/missions/{id}/cancel call")
    status = "cancelled"
    missiondb.update_mission_status(id, status)
