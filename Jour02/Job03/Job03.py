import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    database = "laplateforme"
)

mycursor = db.cursor()
mycursor.execute("SELECT SUM(superficie) AS superficie_totale FROM etage")

res = mycursor.fetchall()

for line in res:
    print(line)
print("La superficie de La Plateforme est de",res,"m2")