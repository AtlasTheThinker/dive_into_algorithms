import math

def binary_search(sorted_list, target):
    upper_bound = len(sorted_list)
    lower_bound = 0
    guess = math.floor(len(sorted_list) / 2)
    while abs(sorted_list[guess] - target) > 0.0001:
        if(sorted_list[guess] < target):
            upper_bound = guess
            guess = math.floor((upper_bound + lower_bound) / 2)
        if(sorted_list[guess] > target):
            lower_bound = guess
            guess = math.floor((upper_bound + lower_bound) / 2)
    return guess

cabinet = [1,2,3,4,5,6,7,8,9,10]
guess = binary_search(cabinet, 6)
print(guess, cabinet[guess])