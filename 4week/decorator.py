import time




def test1(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time is  %s" %(stop_time - start_time  ))


@test1
def bar():
    time.sleep(3)
    print("I'here, I'm bar")