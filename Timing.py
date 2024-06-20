import time
t=time.localtime()
clock=time.strftime('%Y:%m:%d:%H:%M:%S',t)
print(clock)
start=time.time()
for i in range(1,5):
    print(i)
print(time.time()-start)
