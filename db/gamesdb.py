import psycopg2
import sqlalchemy as db

#DB CLASS USING SQLALCHEMY - VERSION 1
class GamesAlchemyDB:
    engine = None 
    conn = None
    def __init__(self):
        try:
            database="etlgamesdb"
            user="postgres"
            host="localhost"
            password="1234"
            port=5433
            
            db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
            self.engine = db.create_engine(db_url)
            self.conn = self.engine.connect()
            print(f"connection done.")
            
        except ConnectionError as e:
            self.engine = None
            print(f"{e}")
        
enginedb = GamesAlchemyDB()

#DB CLASS USING PSYCOPG2 - VERSION 2
class GamesDB:
    connection = None 
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                database="etlgamesdb",
                user="postgres",
                host="localhost",
                password="1234",
                port=5433)
            print(f"connection done.")
        except ConnectionError as e:
            print(f"{e}")    
           
gamedb = GamesDB()