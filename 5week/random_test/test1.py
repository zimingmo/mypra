import random

checkcode = ''
num = 0
while num <= 3:

    for i in range(4):
        current = random.randint(1,4)

        if current == i:
            tmp = chr(random.randint(65, 90))



        else:
            tmp = random.randint(0, 9)

        checkcode += str(tmp)

print(checkcode)