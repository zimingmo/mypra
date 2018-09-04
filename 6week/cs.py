
class Role(object):
    def __init__(self, name, role, weapon, life_value = 100, money = 15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot..")

    def buy_gun(self, gun_name):
        print("%s just bought %s" %(self.name,gun_name))


r1 = Role('Alex', 'police', 'ak47')
r2 = Role('Jack', 'terrorist', 'm4a1')
r3
Role.buy_gun(r3,'123')