from db_connection import DB_connection

db_connection = DB_connection()

class MissionDB:
    def __init__(self, instance: DB_connection):
        self.instance = instance

    def creat_mission(self, data):

        try:
            connection = self.instance.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            insert into missions
            (title, description, location)
            values(%s, %s, %s);
                """,
            (data["title"], data["description"], data["location"] )
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

            cursor.execute(
                """
            update missions
            set assigned_agent_id = %s
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
            select count(*) from missions where status = "in progress" where id = %s
                """
            )

            result = cursor.fetchone()
            print(result)
            return result
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()


    def count_all_missions(self):
        pass

    def count_by_status(self, status):
        pass

    def count_open_missions(self):
        pass

    def count_critical_missions(self):
        pass

    def get_top_agent(self):
        pass





# for testing the methods.            
# d = {"title": "drawing","description": "to draw soldiers","location": "Jerusalem"}
# missiondb = MissionDB(db_connection)
# missiondb.creat_mission(d)