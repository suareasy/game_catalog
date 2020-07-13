import yaml
import psycopg2 as pg

import util

credentials = util.readYAML( 'credentials' )['database']

con = pg.connect( 
    database = credentials['database'], 
    user = credentials['user'], 
    password = credentials['password'], 
    host = "127.0.0.1", 
    port = "5432"
)

con.set_isolation_level( pg.extensions.ISOLATION_LEVEL_AUTOCOMMIT )

cursor = con.cursor()

cursor.execute( 'Drop database if exists game_catalog' )
# cursor.execute( open( 'sql/setup.sql', 'r' ).read())
cursor.close()
con.close()



