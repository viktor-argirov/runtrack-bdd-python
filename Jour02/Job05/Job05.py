import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    database = "laplateforme"
)

mycursor = db.cursor()
mycursor.execute("SELECT Sum(superficie) AS superficie_totale FROM etage")

res = mycursor.fetchone()

print("La superficie de La Platforme est de",res[0],"m2")