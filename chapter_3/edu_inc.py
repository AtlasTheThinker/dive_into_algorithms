import math
import matplotlib.pyplot as plt

THRESHOLD = 0.00001
MAX_ITERATIONS = 100000
STEP_SIZE = 0.0001

def income(edu_yrs):
    return math.sin((edu_yrs - 10.6) * (2 * math.pi / 4)) + (edu_yrs - 11) / 2

def income_derivative(edu_yrs):
    return math.cos((edu_yrs - 10.6) * (2 * math.pi / 4)) + 1 / 2

def income_derivative_flipped(edu_yrs):
    return 0 - income_derivative(edu_yrs)

current_edu = 11
keep_going = True
iterations = 0
while(keep_going):
    edu_change = STEP_SIZE * income_derivative(current_edu)
    current_edu += edu_change
    if abs(edu_change) < THRESHOLD or iterations >= MAX_ITERATIONS:
        keep_going = False
    iterations += 1
print(current_edu)
xs = [11 + x / 100 for x in list(range(901))]
ys = [income(x) for x in xs]
plt.plot(xs,ys)
plt.plot(current_edu, income(current_edu), 'ro')
plt.title('Education and Income')
plt.xlabel('Years of Education')
plt.ylabel('Lifetime income')
plt.show()