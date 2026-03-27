import time
def deco(func):
    def inner_fun():
        start=time.time()
        print(start)
        func()
        end=time.time()
        print(end)
    return inner_fun

@deco
def mytest():
    print("hello")
print(mytest())