import sqlite3
import random
import time

class Mob:
    def __init__(self,ID):
        self.ID = ID
        
        db = sqlite3.connect("dbname")
        cur = db.cursor()

        cur.excute("SELECT * FROM Mobs WHERE ID=?",(self.ID,))
        result = cur.fetchall()

        self.speed = result[2]
        self.health = result[3]

    def hit(self, damage):
        if self.health > 0:
            self.health -= damage
        else:
            self.dead()

    def slow(self, amount):
        if (self.speed-amount) > 0:
            self.speed -= amount
        else:
            self.speed = 1

    def dps(self, amount):
        for i in range(0,2):
            if self.health > 0:
                self.health -= amount
                time.sleep(1)
            else:
                self.dead()
                break

    def dead():
        pass

class Tower:
    def __init__(self, ID):
        self.ID = ID

        db = sqlite3.connect("dbname")
        cur = db.cursor()

        cur.execute("SELECT * FROM Towers WHERE ID=?", (self,ID,))
        result = cur.fetchall()

        self.proj_list = []

        self.power = result[2]
        self.range = result[3]
        self.fire_rate = result[4]
        self.spec = result[5] #the type of the tower
        self.amount = result[6] #amount of slow/critical/max hp dps/number of targets to hit

        if self.spec == "ice":
            self.ice_hit(self.amount)
        elif self.spec== "critical":
            self.critical(self.amount)
        elif self.spec == "poison":
            self.poison_hit(self.amount)
        elif self.spec == "aoe":
            self.aoe_hit(self.amount)

    def ice_hit(self, amount):
        self.proj_list = [self.power, self.amount, self.spec]

    def critical_hit(self, amount):
        if amount == 50:
            self.crit = random.randint(0,1)
            if self.crit == 1:
                self.proj_list =[self.power*2, 0, self.spec]
            else:
                self.proj_list =[self.power, 0, self.spec]
            
        if amount == 25:
            self.crit = random.randint(0,3)
            if self.crit == 1:
                self.proj_list = [self.power*2, 0, self.spec]
            else:
                self.proj_list = [self.power, 0, self.spec]

        if amount == 75:
            self.crit = random.randint(0,3)
            if self.crit == 0:
                self.proj_list = [self.power, 0, self.spec]
            else:
                self.proj_list = [self.power*2, 0, self.spec]

    def poison_hit(self, amount):
        self.proj_list = [self.power, self.amount, self.spec]

    def aoe_hit(self, amount):
        self.proj_list = [self.power, self.amount, self.spec]

class Projectile:
    def __init__(self, proj_list, mob):
        self.power = proj_list[0]
        self.amount = proj_list[1]
        self.spec = proj_list[2]

        if spec == "ice":
            mob.slow(self.amount)
            mob.hit(self.power)

        elif spec == "poison":
            mob.hit(self.power)
            mob.dps(self.amount)

        elif spec == "aoe":
            mob.hit(self.power)
            pass #to add code that will apply mob.hit to nearby mobs - shouldn't be that hard hopefuly:D

        else:
            mob.hit(self.power)


###   Test   ###
if __name__ == "__main__":
    pig_m = Mob(1) # m for mob
    basic_t = Tower(1) # t for tower/turret




            
            

        
        
        
        
        
                
        
        
           
