from sqlmodel import create_engine, SQLModel

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
            connect_args = {"check_same_thread": False}
            self.engine = create_engine(db_url, connect_args=connect_args)
            
        except ConnectionError as e:
            self.engine = None
            print(f"{e}")
        
    def create_db_and_tables():
        SQLModel
    
enginedb = GamesAlchemyDB()