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
        pass

    def get_mission_by_id(self, id):
        pass

    def assign_mission(self, m_id, a_id):
        pass

    def update_mission_status(self, id, status):
        pass

    def get_open_missions_by_agent(self, id):
        pass

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