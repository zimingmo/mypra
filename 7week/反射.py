

class Dog(object):

    def __init__(self, name):
        self.name = name


    def eat(self):
        print("%s is eating..." % self.name)

d = Dog("NiuHanYang")
choice = input(">>:").strip()



if hasattr(d, choice):
    getattr(d, choice)()
else:
    print("not such func")