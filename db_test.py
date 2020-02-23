import sqlite3
 
con = sqlite3.connect('harga.db')
 
def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT * FROM price_list')
 
    rows = cursorObj.fetchall()
 
    for row in rows:
        
        print(row[2])
        
 
sql_fetch(con)
con.close()