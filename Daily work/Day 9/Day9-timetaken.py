from threading import*
import time
def f1(n):
    for x in range(n):
        time.sleep(4)
        print(x)
start=time.time()

def f2():
    for x in range(6,11):
        time.sleep(3)
        print(x)
f1()
f2()
end=time.time()
print('time taken',end-start)