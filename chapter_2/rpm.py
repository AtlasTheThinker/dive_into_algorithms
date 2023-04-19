import math
import pandas as pd

n1 = int(input())
n2 = int(input())

halving = [n1]
doubling = [n2]
iterations = 0
while(min(halving) > 1):
    iterations += 1
    halving.append(math.floor(min(halving)/2))
    
while(len(doubling) < len(halving)):
    iterations += 1
    doubling.append(max(doubling) * 2)
    
half_double = pd.DataFrame(zip(halving, doubling))

half_double = half_double.loc[half_double[0] % 2 ==1,:]

answer = sum(half_double.loc[:,1])
print(iterations, answer)