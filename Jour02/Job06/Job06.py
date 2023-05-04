import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    database = "laplateforme"
)

mycursor = db.cursor()
mycursor.execute(" SELECT SUM(capacite) AS capacite_totale FROM salles")

res = mycursor.fetchone()


print("La capacite de toutes les salles est de :",res[0])