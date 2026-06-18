from fastapi import APIRouter, HTTPException
from database.mission_db import missiondb
from model.mission_model import Mission


router = APIRouter(prefix="/missions", tags=["missions"])


@router.post("/missions")
def creat_mission(data: Mission):
    return missiondb.creat_mission(data)


@router.get("/missions")
def get_all_missions():
    return missiondb.get_all_missions()


@router.get("/missions/{id}")
def get_mission_by_id(id: int):
    return missiondb.get_mission_by_id(id)


@router.put("/missions/{id}/assign/{agent_id}")
def assign_mission(id: int, agent_id: int):
    return missiondb.assign_mission(id, agent_id)


@router.put("/missions/{id}/start")
def update_mission_status(id: int):
    status = "in_progress"
    missiondb.update_mission_status(id, status)


@router.put("/missions/{id}/complete")
def update_mission_status():
    status = "completed"
    missiondb.update_mission_status(id, status)


@router.put("/missions/{id}/fail")
def update_mission_status():
    status = "failed"
    missiondb.update_mission_status(id, status)


@router.put("/missions/{id}/cancel")
def update_mission_status():
    status = "cancelled"
    missiondb.update_mission_status(id, status)
