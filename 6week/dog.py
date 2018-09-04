class Dog(object):
    def __init__(self, name):
        self.name = name

    def bulk(self):
        print("%s:wang wang wang" % self.name)



d1 = Dog("daerduo")
d2 = Dog('babababa')
d3 = Dog('112233')
d4 = Dog('papapap')

d1.bulk()
d2.bulk()
d3.bulk()
d4.bulk()