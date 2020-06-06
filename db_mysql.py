import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="vmanz73",
  passwd="vmanz1997",
  database="sayur"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM `price` ORDER BY `tanggal` DESC LIMIT 6")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)