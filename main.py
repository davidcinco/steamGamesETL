from ETL.etl import ETLGames
# from db.gamesdb import gamedb

etl = ETLGames()

def runETL():
    #extract
    result = etl.extractGames()
    #transform
    filteredGames = etl.transformGames(result)
    #loads
    etl.loadGames(filteredGames)
    
    print("ETL Pipeline finished.")

runETL()