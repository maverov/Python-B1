__author__ = "William Read"
__version__ = "1.0"

import sqlite3

class Turret_Data:

    def __init__(self):
        self.conn = sqlite3.connect("pixeldatabase.db")
        self.cur = conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS turrets(ID INTEGER, Name TEXT, Power INTEGER, Range REAL, FireRate REAL)")

    def create_turret(self, ID, Name, Power, Range, FireRate):
        self.cur.execute("INSERT INTO turrets VALUES(?,?,?,?)",(ID,Name,Power,Range,FireRate))

    def query_turret(self, ID):
        self.cur.execute("SELECT * FROM turrets WHERE ID=?",(ID,))
        self.data = self.cur.fetchall()

    def return_turret_query():
        return self.data

class Mob_Data:

    def __init__(self):
        self.conn = sqlite3.connect("pixeldatabase.db")
        self.cur = conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS mobs(ID INTEGER, Name TEXT, Speed REAL, Health INTEGER)")

    def create_mob(self,ID,Name,Speed,Health):
        self.cur.execute("SELECT * FROM mobs WHERE ID=?",(ID,))
        self.data = self.cur.fetchall()

    def query_mob(self, ID):
        self.cur.execute("SELECT * FROM turrets WHERE ID=?",(ID,))
        self.data = self.cur.fetchall()

    def return_mob_query():
        return self.data

if __name__ == "__main__":
    pass
