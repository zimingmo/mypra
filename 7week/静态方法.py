class Dog(object):

    def __init__(self, name):
        self.name = name
        self.__food = None

   # @staticmethod
   # @classmethod
    @property
    def eat(self):
        print("%s is eating %s " %(self.name, self.__food))

    @eat.setter
    def eat(self, food):
        print("set to food:")
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("del to food")

    def talk(self):
        print("%s is talking" % self.name)

d = Dog("chengRongHua")
d.talk()

d.eat
d.eat = "baozi"
d.eat