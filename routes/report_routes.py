from fastapi import APIRouter
from database.agent_db import agentdb
from database.mission_db import missiondb

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/reports/summary")
def get_summary():

    summary ={}
            
    summary["active_agents_count"] = agentdb.agents_active_count()
    summary["total_missions"] = missiondb.count_all_missions()
    summary["open_missions"] = missiondb.count_open_missions()
    summary["completed_missions"] = missiondb.count_by_status("completed")
    summary["failed_missions"] = missiondb.count_by_status("failed")
    summary["critical_missions"] = missiondb.count_critical_missions()

    return summary


@router.get("/reports/missions-by-status")
def get_missions_by_status():

    missions = {}

    missions["open"] = missiondb.count_by_status("assigned")
    missions["in_progress"] = missiondb.count_by_status("in_progress")
    missions["completed"] = missiondb.count_by_status("completed")
    missions["failed"] = missiondb.count_by_status("failed")
    missions["cancelled"] = missiondb.count_by_status("cancelled")

    return missions



@router.get("/reports/top-agent")
def get_top_student():
    return missiondb.get_top_agent()











