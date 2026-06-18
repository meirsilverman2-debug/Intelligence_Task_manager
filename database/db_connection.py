import mysql.connector

class DB_connection:

    def get_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            port=3306,
            password="1234",
            database="Intelligence_db"
        )
    
    def create_database(self):
        try:
            connection = self.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            create database if not exists Intelligence_db ;
                """
            )


            print("The database as been created right now or it is already exists")

            return {"message": "the database as been created right now or it is already exists"}

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
        
        


    def create_tables(self):
        try:
            connection = self.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                """
            create table if not exists agents(
            id int auto_increment primary key,
            name varchar(100) not null,
            specialty varchar(100) not null,
            is_active boolean default True,
            completed_missions int default 0,
            failed_missions int default 0,
            agent_rank enum ('Junior', 'Senior', 'Commander') not null default 'Junior')
            ;
            create table if not exists missions(
            id int auto_increment primary key,
            title varchar(100) not null,
            description text,
            location varchar(100),
            difficulty int,
            importance int,
            status varchar(100) default "new",
            risk_level varchar(100),
            assigned_agent_id int default null
            );
                """
            )

            print("The two tables have been created right now or they are already exists")
            return {"message": "the two tables have been created right now or they are already exists"}
            
        except Exception as e:
            print(e)

        finally:
            cursor.close()
        
            
# # for testing the methods in the class.
# db_connection = DB_connection()
# db_connection.create_database()
# db_connection.create_tables()