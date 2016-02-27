__author__      = "Hristiyan Maverov, Catalin Cojocariu"
__copyright__   = "Copyright 2016"

import sqlite3
import random

conn = sqlite3.connect ('pixeldatebase.db')
c = conn.cursor()

def turret_table():
	c.execute ('CREATE TABLE IF NOT EXISTS turret(Id REAL, Name TEXT, Power REAL, Range REAL, FireRate REAL)')

def data_turret():
	c.execute("INSERT INTO turret VALUES(1, 'Fire Turret', 50, 100, 30)")
	conn.commit()
	
def read_turret():
        c.execute("SELECT * FROM turret")
        #data = c.fetchall()
        #print(data)
        for row in c.fetchall():
                print(row)

def mob_table():
	c.execute('CREATE TABLE IF NOT EXISTS mob(Id REAL, Name TEXT, Speed REAL, Health REAL)')

def data_mob():
	c.execute("INSERT INTO mob VALUES(1, 'First Mob', 20, 100)")
	conn.commit()
	c.close()
	conn.close()

def read_mob():
        c.execute("SELECT * FROM mob")
        #data = c.fetchall()
        #print(data)
        for row in c.fetchall():
                print(row)

turret_table()
data_turret()
mob_table()
data_mob()
