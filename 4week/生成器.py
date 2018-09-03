import time

def consumer(name):
    print("%s 准备吃包子了！" %name)
    while True:
        baozi = yield
        print("包子[%s]来了，被[%s]吃了!" %(baozi, name))

c  = consumer("ChenRongHua")
# next(c)
# b1 = '韭菜'
# c.send(b1)
# next(c)
def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    next(c)
    next(c2)
    print('开始做包子了！')
    for i in range(10):
        time.sleep(1)
        print('做了两个包子！')
        c.send(i)
        c2.send(i)

producer('alex')