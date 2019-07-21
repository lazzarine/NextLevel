import time
start_time = time.time()
for i in range(10000):
    x=1
    print(x)
elapsed_time = time.time() - start_time
print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))),
