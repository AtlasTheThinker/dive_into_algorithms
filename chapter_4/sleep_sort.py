import random
import threading
from time import sleep

def sleep_sort(i):
    sleep(i)
    global sorted_list
    sorted_list.append(i)
    return i

items = [int(100 * random.random()) for x in range(51)]
sorted_list = []
ignore_results = [threading.Thread(target = sleep_sort, args = (i, )).start() for i in items]
print(sorted_list)