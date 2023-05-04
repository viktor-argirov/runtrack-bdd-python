import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    database = "laplateforme"
)

mycursor = db.cursor()
mycursor.execute( CREATE TABLE etage(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL ,
    numero INTEGER NOT NULL ,
    superficie INTEGER NOT NULL
    );")

res = mycursor.fetchall()

for line in res:
    print(line)

#############################################

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    database = "laplateforme"
)

mycursor = db.cursor()
mycursor.execute(CREATE TABLE salles(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL ,
    id_etage INTEGER NOT NULL ,
    capacite INTEGER NOT NULL
    );

res = mycursor.fetchall()

for line in res:
    print(line)