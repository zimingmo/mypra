

import sys, os
print(sys.path)

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from module_alex import name


 print(module_alex.name)
module_alex.say_hello()


def logger():
    print('in the main')
logger()