import mysql.connector
import pandas as pd 
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="vmanz73",
  passwd="vmanz1997",
  database="sayur"
)
def data():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT `nama_sayur`, `harga`, `tanggal` FROM `price` ORDER BY `tanggal` DESC LIMIT 6")
    myresult = mycursor.fetchall()
    
    df = pd.DataFrame(myresult) 
    df.columns = ["Nama_sayur", "harga", "tanggal"]
    df.to_csv ('dataframe.csv', index = False, header=True)
    return df
    