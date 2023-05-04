import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    database = "laplateforme"
)

mycursor = db.cursor()
mycursor.execute(" SELECT employes.nom,employes.prenom,employes.id_service,\
services.nom FROM employes JOIN services WHERE employes.id=services.id;")

res = mycursor.fetchone()

class employes:
    def __init__(self,nom,prenom,salaire,id_service):
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire
        self.id_service=id_service

    def read(self, id):
        sql = "SELECT * FROM employes WHERE id = ?"
        self.cursor.execute(sql, (id,))
        return self.cursor.fetchone()
   
    def delete(self, id):
        sql = "DELETE FROM employes WHERE id = ?"
        self.cursor.execute(sql, (id,))
        self.conn.commit()
        return self.cursor.rowcount