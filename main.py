from fastapi import FastAPI
from routes.agent_routes import router as agent_router
from routes.mission_routes import router as mission_router
from routes.report_routes import router as report_router
from database.db_connection import DB_connection

app = FastAPI()


db_connection = DB_connection()
db_connection.create_database()
db_connection.create_tables()


# all three routers:
app.include_router(agent_router)
app.include_router(mission_router)
app.include_router(report_router)
