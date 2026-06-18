from .db_connection import DB_connection
from model.agent_model import Agent


db_connection = DB_connection()

class AgentDB:

    def __init__(self, instance: DB_connection):
        self.instance = instance

    def create_agent(self, data: Agent):
        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            insert into agents(name, specialty) values(%s, %s);
                """,
                (data.name, data.specialty)
            )

            connection.commit()
            print("A new agent as been created wow!")

            # connection.commit()
            # cursor.close()

            # cursor = connection.cursor(dictionary=True)
            cursor.execute(
                """
            SELECT * FROM agents 
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


    def get_all_agents(self):
        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select * from agents ;
                """
            )

            result = cursor.fetchall()
            return result

        except Exception as e:
            print(e)

        finally:
            cursor.close()
       

    def get_agent_by_id(self, id):
        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select * from agents where id = %s ;
                """,
                (id,)
            )

            result = cursor.fetchone()
            return result

        except Exception as e:
            print(e)

        finally:
            cursor.close()


    def update_agent(self, id, data: Agent):
        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            update agents 
            set name = %s,
            specialty = %s,
            agent_rank = %s
            where id = %s
                """,
                (data.name, data.specialty, data.agent_rank, id)
            )

            connection.commit()
            print(f"The agent with the {id} id has been updated")
            return {"message": f"The agent with the {id} id has been updated"}

        except Exception as e:
            print(e)

        finally:
            cursor.close()


    def deactivate_id(self, id):
        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            update agents
            set is_active = %s
            where id = %s ;
                """,
                (False, id)
            )

            connection.commit()
            print(f"The agent with the id {id} has been deactivate")
            return {"message": f"The agent with the id {id} has been deactivate"}
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()


    def increment_completed(self, id):
        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            update agents
            set completed_missions = completed_missions + 1
            where id = %s
                """,
                (id,)
            )

            connection.commit()
            print("comleted_missions have been increment by one")
            return {"message": "comleted_missions have been increment by one"}
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()


    def increment_failed(self, id):
        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                """
            update agents
            set failed_missions = failed_missions + 1
            where id = %s ;
                """,
                (id,)
            )
            
            connection.commit()
            print(f"Failed missions that belongs to agent with the id {id} has been increment by one")
            return {"message": f"Failed missions that belongs to agent with the id {id} has been increment by one"}
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()   
        

    def get_agent_performance(self, id):
        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select (completed_missions) as completed from agents where id = %s ;
                """,
                (id,)
            )
            copmleted = cursor.fetchone()
            print(copmleted)

            cursor.execute(
                """
            select (failed_missions) as failed from agents where id = %s ;
                """,
                (id,)
            )
            failed = cursor.fetchone()
            print(failed)

            cursor.execute(
                """
            select concat(completed_missions + failed_missions) as total from agents where id = %s ;
                """,
                (id,)
            )
            total = cursor.fetchone()
            for v in total.values():
                v = int(v)
            total["total"] = v
            print(total)

            cursor.execute(
                """
            select count(*)as total from missions where assigned_agent_id = %s ;
                """,
                (id,)
            )

            total2 = cursor.fetchone()
            print(total2)
            
            num_of_missions = 0
            for v in total2.values():
                num_of_missions += v

            total["total"] += num_of_missions

            success_rate = (sum(copmleted.values()) / sum(total.values())) * 100
            print(success_rate)

            print("It works all right!!!")
            result = {"completed": copmleted, "failed": failed, "total": total, "success": success_rate}
            print(result)
            return result

        except Exception as e:
            print(e)

        finally:
            cursor.close()


    def agents_active_count(self):
        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            select count(*)as active_ageents from agents where is_active = True ;
                """
            )

            result = cursor.fetchall()
            print("It works")
            print(result)
            return result
        
        except Exception as e:
            print(e)

        finally:
            cursor.close


# for testing the methods.

agentdb = AgentDB(db_connection)

d = {"name": "Mimi", "specialty": "singing"}
agentdb.create_agent(d)

# agentdb.get_agent_performance(1)

# agentdb.agents_active_count()