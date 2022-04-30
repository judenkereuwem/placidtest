import time

start = time.time()
finish = start + 2
while time.time() < finish:
    print("work")
    print(finish - start)
