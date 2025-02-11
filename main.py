from ETL.etl import ETLGames
# from db.gamesdb import gamedb

etl = ETLGames()

def runET():
    #extract
    result = etl.extractGames()
    #transform
    filteredGames = etl.transformGames(result)
    print(filteredGames.head())
    #loads
    etl.loadGames(filteredGames)
    
    print("ETL Pipeline finished.")

runET()