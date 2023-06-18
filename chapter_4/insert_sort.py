import random
import math
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np

def insert_cabinet(cabinet, to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0
    global step_counter
    while check_location >= 0:
        step_counter += 1
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = -1
        check_location -= 1
    cabinet.insert(insert_location, to_insert)
    step_counter += 1
    return cabinet

def insertion_sort(cabinet):
    new_cabinet = []
    global step_counter
    while len(cabinet):
        step_counter += 1
        new_cabinet = insert_cabinet(new_cabinet, cabinet.pop(0))
    return new_cabinet

def check_steps(size_of_cabinet):
    cabinet = [int(1000 * random.random()) for i in range(size_of_cabinet + 1)]
    global step_counter
    step_counter = 0
    insertion_sort(cabinet)
    return step_counter
    
step_counter = 0
random.seed(5040)
xs = list(range(1, 100))
ys = [check_steps(x) for x in xs]
ys_exp  = [math.exp(x) for x in xs]
plt.plot(xs, ys)
axes = plt.gca()
axes.set_ylim([np.min(ys), np.max(ys) + 140])
plt.plot(xs, ys_exp)
plt.title('Insertion sort complexity growth compared to exp function')
plt.xlabel('Array size')
plt.ylabel('Number of steps')
plt.show()
print(ys)