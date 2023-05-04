import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    database = "laplateforme"
)

mycursor = db.cursor()
mycursor.execute("SELECT * FROM etudiants")

res = mycursor.fetchall()

for line in res:
    print(line)