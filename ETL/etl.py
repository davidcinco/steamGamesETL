import pandas as pd 

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
            steamGames = steamdf[["name", "developers", "publishers", "is_released", "release_date", 
            "total_reviews", "total_positive", "total_negative", "review_score", "positive_percentual", 
            "metacritic", "is_free", "price_initial (USD)"]]
            
            return steamGames        
            
            
    def loadGames(self):
        try:
            pass
        except Exception as e:
            print(f"{e}")
    
