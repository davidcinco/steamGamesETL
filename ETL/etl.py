import pandas as pd 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

gamedf = pd.read_csv("../csv/steam_games.csv")
print (gamedf.columns)

def getGamesAvailable():
    games = gamedf[["steam_appid", "name", "developers", "publishers", "genres", "required_age", "is_released", "release_date", "review_score", "metacritic", "is_free", "price_initial (USD)"]]   
    print(games.head())
    
getGamesAvailable()