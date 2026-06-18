from .db_connection import DB_connection
from model.mission_model import Mission
from fastapi import HTTPException
from .agent_db import agentdb



db_connection = DB_connection()
agentdb

class MissionDB:
    def __init__(self, instance: DB_connection):
        self.instance = instance

    def creat_mission(self, data: Mission):

        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            level_risk = data.difficulty * 2 + data.importance
            risk_level = ""

            if  17 >= level_risk >= 10 :
                risk_level = "MEDIUM"

            elif 18 >= level_risk >= 24:
                risk_level = "HIGH"

            elif level_risk >= 25 :
                risk_level = "CRITICAL"
            
            else:
                risk_level = "low"


            if 1 > data.importance > 10 :
                raise HTTPException(403, "you are forbidden from entering importance numbers that are  smaller than one and more than greater") 

            if 1 > data.difficulty > 10 :
                raise HTTPException(403, "you are forbidden from entering difficulty numbers that are  smaller than one and more than greater") 

            cursor.execute(
                """
            insert into missions
            (title, description, location, difficulty, importance, risk_level)
            values(%s, %s, %s, %s, %s, %s);
                """,
            (data.title, data.description, data.location, data.difficulty, data.importance, risk_level)
            )

            connection.commit()
            cursor.close()

            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                """
            SELECT * FROM missions  
            ORDER BY id 
            DESC
            LIMiT 1 ;
 
                """
            )

            result = cursor.fetchone()

            print(result)
            return result
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

    def get_all_missions(self):
        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select * from missions ;
                """
            )

            result = cursor.fetchall()
            print(result)
            return result
        
        except Exception as e:
            print(e)

        finally:
            cursor.close()

    def get_mission_by_id(self, id):
        try: 
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select * from missions where id = %s
                """,
                (id,)
            )

            result = cursor.fetchone()
            print(result)
            return result
        
        except Exception as e:
            print(e)

        finally:
            cursor.close()

    def assign_mission(self, m_id, a_id):
        try: 
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            agent = agentdb.get_agent_by_id(a_id)
            print(agent)
            mission = self.get_mission_by_id(m_id)
            print(mission)

            if agent["is_active"] == False:
                raise HTTPException(403, "you cannot assigned missions to an agent that is not active you need to understand it")

            if agent["agent_rank"] != "Commander"  and mission["risk_level"] == "critical" :
                raise HTTPException(403, "an agent with the rank lower than commander cannot take a mission with risk level fo critical")
            
            if mission["status"] != "new":
                raise HTTPException(403, "you cannot assigned a mission unless its status is 'new' understood")


            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            update missions
            set assigned_agent_id = %s,
            status = 'assigned'
            where id = %s
                """,
                (a_id, m_id)
            )

            connection.commit()
            return {"message": f"the mission with the id {m_id} was assigned to agent with id {a_id} successfuly!"}
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
        

    def update_mission_status(self, id, status):

        try: 
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select * from missions where id = %s
                """,
                (id,)
            )

            data = cursor.fetchone()
            if status == "cancelled" and data["status"] == "new" or data["status"] == "in_progress":
                raise HTTPException(403,"you are forbidden to cancelled a mission while it is in progress or a new mission ok")
            
            elif status == "completed" or status == "failed" and data["status"] != "in_progress":
                raise HTTPException(403,"you are forbidden to finish the mission or deem it failed mission when it is any other status rather than in_progress ")

            cursor.execute(
                """
            update missions
            set status = %s
            where id = %s
                """,
                (status, id)
            )

            connection.commit()
            return {"message": f"the status of mission {id} was changed into {status}"}
        
        except Exception as e:
            print(e)

        finally:
            cursor.close()
        

    def get_open_missions_by_agent(self, id):
        try: 
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select count(*) as open_missions_by_agent from missions where id = %s and status = "in progress" 
                """,
                (id,)
            )

            result = cursor.fetchone()
            print(result)
            return result
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()


    def count_all_missions(self):
        try: 
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select count(*) as all_missions from missions
                """
            )

            result = cursor.fetchall()

            print(result)
            return result
        
        except Exception as e:
            print(e)

        finally:
            cursor.close

    def count_by_status(self, status):
        try: 
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select count(*) as missions_by_status from missions where status = %s
                """,
                (status,)
            )

            result = cursor.fetchone()
            print(result)
            return result

        except Exception as e:
            print(e)

        finally:
            cursor.close()

    def count_open_missions(self):
        try: 
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select count(*) as open_missions from missions where status = "assigned" or status = "in_progress" or status = "new"
                """
            )

            result = cursor.fetchone()
            print(result)
            return result

        except Exception as e:
            print(e)

        finally:
            cursor.close()


    def count_critical_missions(self):
        try: 
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select count(*) as all_critical_missions from missions where difficulty = "critical"
                """
            )

            result = cursor.fetchone()
            print(result)
            return result
        
        except Exception as e:
            print(e)

        finally:
            cursor.close()


    def get_top_agent(self):
        try: 
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select max(completed_missions) as top_completed_missions, (name) as top_agent
            from agents 
            group by name 
            limit 1 
                """
            )

            result = cursor.fetchone()
            print(result)
            return result
        
        except Exception as e:
            print(e)

        finally:
            cursor.close()



missiondb = MissionDB(db_connection)

# for testing the methods.
             
# d = {"title": "drawing","description": "to draw soldiers","location": "Jerusalem"}
# missiondb.creat_mission(d)
# missiondb.assign_mission(1, 1)
# missiondb.count_all_missions()
# missiondb.count_by_status("new")
# missiondb.count_critical_missions()
# missiondb.get_top_agent()
# missiondb.get_mission_by_id(1)
# missiondb.update_mission_status(3,"in_progress")
# missiondb.count_open_missions()
# missiondb.get_open_missions_by_agent(1)