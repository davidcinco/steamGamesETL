from ETL.etl import ETLGames
from db.gamesdb import gamedb

def runET():
    #e
    result = ETLGames().extractGames()
    #t
    ETLGames().transformGames(result)
    
