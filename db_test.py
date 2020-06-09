import sqlite3
 
con = sqlite3.connect('harga.db')
 
def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT * FROM price_list')
    
    rows = cursorObj.fetchall()

    
sql_fetch(con)
con.close()