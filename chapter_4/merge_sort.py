import random
import math

def merging(left, right):
    new_cabinet = []
    while min(len(left), len(right)):
        if left[0] <= right[0]:
            to_insert = left.pop(0)
            new_cabinet.append(to_insert)
        elif left[0] > right[0]:
            to_insert = right.pop(0)
            new_cabinet.append(to_insert)
    if not len(left):
        new_cabinet.extend(right)
    if not len(right):
        new_cabinet.extend(left)
    return new_cabinet

def mergesort(cabinet):
    new_cabinet = []
    if len(cabinet) == 1:
        new_cabinet = cabinet
    else:
        left = mergesort(cabinet[:math.floor(len(cabinet) / 2)])
        right = mergesort(cabinet[math.floor(len(cabinet) / 2):])
        new_cabinet = merging(left, right)
    return new_cabinet

cabinet = [int(10000 * random.random()) for x in range(100001)]
print(mergesort(cabinet))