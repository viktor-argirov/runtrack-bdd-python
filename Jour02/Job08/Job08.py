import mysql.connector

class ZooDAO:
    def __init__(self, db_file):
        self.conn = mysql.connector.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS animaux (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                race TEXT,
                id_cage INTEGER,
                naissance DATE,
                origin TEXT,
                FOREIGN KEY (id_cage) REFERENCES cages(id)
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                superficie REAL,
                capacite INTEGER
            );
        """)
        self.conn.commit()

    def ajouter_animal(self, nom, race, id_cage, naissance, origin):
        sql = """
            INSERT INTO animaux (nom, race, id_cage, naissance, origin)
            VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(sql, (nom, race, id_cage, naissance, origin))
        self.conn.commit()

    def supprimer_animal(self, id_animals):
        sql = "DELETE FROM animaux WHERE id = ?"
        self.cursor.execute(sql, (id_animals,))
        self.conn.commit()

    def modifier_animal(self, id_animal, nom, race, id_cage, naissance, origin):
        sql = """
            UPDATE animaux
            SET nom = ?, race = ?, id_cage = ?, naissance = ?, origin = ?
            WHERE id = ?
        """
        self.cursor.execute(sql, (nom, race, id_cage, naissance, origin, id_animal))
        self.conn.commit()

    def afficher_animaux(self):
        sql = """
            SELECT a.id, a.nom, a.race, a.naissance, a.origin, c.id, c.superficie, c.capacite
            FROM animaux a
            LEFT JOIN cages c ON a.id_cage = c.id
        """
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            print(f"Animal n°{row[0]} : {row[1]} ({row[2]}) né le {row[3]}, originaire de {row[4]}, cage n°{row[5]} (superficie : {row[6]} m², capacité : {row[7]})")

    def afficher_animaux_par_cage(self):
        sql = """
            SELECT c.id, c.superficie, c.capacite, GROUP_CONCAT(a.nom, ", ")
            FROM cages c
            LEFT JOIN animaux a ON a.id_cage = c.id
            GROUP BY c.id
        """
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            print(f"Cage n°{row[0]} (superficie : {row[1]} m², capacité : {row[2]}) : {row[3]}")

    def ajouter_cage(self, superficie, capacite):
        sql = """
            INSERT INTO cages (superficie, capacite)
            VALUES (?, ?)
        """
        self.cursor.execute(sql, (superficie, capacite))
        self.conn.commit()

    def supprimer_cage(self, id_cage):
        sql = "DELETE FROM cages WHERE id = ?"
        self.cursor.execute(sql)
