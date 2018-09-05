

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
        print("--doens't run")

    def eat(self):
        print("%s is eating..." %self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

class Relation(object):
    def __init__(self, n1, n2):
        print("init in relation")
    def make_friends(self, obj):
        print("%s is making friends with %s" % (self.name, obj.name))
        self.friends.append(obj.name)

class Man(People, Relation):
    def __init__(self, name, age, money):
       # People.__init__(self, name, age)
        super(Man, self).__init__(name, age)
        self.money = money
        print("%s 一出生就有 %s money" %(self.name, self.money))

    def piao(self):
        print("%s is piaoing ..... 20s....done." % self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping ")

class Woman(People):
    def get_birth(self):
        print("%s is born a baby..." % self.name)

m1 = Man('mysic', 26,1500)
w1 = Woman('mikey', 18)
m1.make_friends(w1)


print(m1.friends)
print(m1.friends)