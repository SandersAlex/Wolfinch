'''
 OldMonk Auto trading Bot
 Desc: highlevel Db Implementation
 (c) Joshith Rayaroth Koderi
'''

# use the specific db impl
from sqlite import SqliteDb

DB = None

def getDb ():
    global DB
    if DB == None:
        #use sqlite now
        DB = SqliteDb()
    return DB
    
#EOF