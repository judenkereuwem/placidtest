import time

start = time.time()
finish = start + 5
while time.time() < finish:
    print("execution complete")
    print(finish - start)
