import pandas as pd 
from db.gamesdb import enginedb

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class ETLGames:
    def __init__(self):
        pass
    
    def extractGames(self):
        try:
            steamdf = pd.read_csv("./csv/steam_games.csv")
            return steamdf
        except FileNotFoundError as fileError:
            print(f"{fileError}")
            return None
        
    def transformGames(self, steamdf):
        if steamdf is not None:
            #get specific columns from csv
            steamGames = steamdf[["name", "developers", "publishers", "is_released", "release_date", 
            "total_reviews", "total_positive", "total_negative", "review_score", "positive_percentual", 
            "metacritic", "is_free", "price_initial (USD)"]]
            
            #rename column to match with our table using SQLAlchemy
            steamGames.rename(columns={"price_initial (USD)": "price_initial"}, inplace=True)
            
            #modify release_date where Not Released value is found"
            steamGames.loc[steamGames["release_date"] == "Not Released", "release_date"] = None 
            
            #modify release_date where Not Released value is found"
            steamGames.loc[steamGames["release_date"] == "Not Released", "release_date"] = None 
            
            
            return steamGames
            
    def loadGames(self, games):
        try:
            games.to_sql("games", enginedb.engine, if_exists="append", index=False)
        except Exception as e:
            print(f"{e}")
    
