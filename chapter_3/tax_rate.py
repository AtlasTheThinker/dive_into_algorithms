import math
import matplotlib.pyplot as plt

STEP_SIZE = 0.001
THRESHOLD = 0.00001
MAX_ITERATIONS = 100_000
IS_FLIPPED = False

def revenue(tax):
    return 100 * (math.log(tax + 1) - (tax - 0.2) ** 2 + 0.04)

def revenue_flipped(tax):
    return 0 - revenue(tax)

def revenue_derivative(tax):
    return 100 * (1 / (tax + 1) - 2 * (tax - 0.2))

def revenue_derivative_flipped(tax):
    return 0 - revenue_derivative(tax)

current_rate = 0.7
keep_going = True
iterations = 0
while(keep_going):
    rate_change = STEP_SIZE * (revenue_derivative(current_rate) if not IS_FLIPPED else revenue_derivative_flipped(current_rate))
    current_rate = current_rate + (rate_change if not IS_FLIPPED else -rate_change)
    
    if abs(rate_change) < THRESHOLD or iterations >= MAX_ITERATIONS:
        keep_going = False
    
    iterations += 1

def show_revenue():
    xs = [x / 1000 for x in range(1001)]
    ys = [revenue(x) for x in xs]
    plt.plot(xs, ys)
    plt.plot(current_rate, revenue(current_rate), 'ro')
    plt.title('Tax Rates and revenue')
    plt.xlabel('Tax Rate')
    plt.ylabel('Revenue')
    print(current_rate)
    plt.show()

def show_revenue_flipped():
    IS_FLIPPED = True
    xs = [x / 1000 for x in range(1001)]
    ys = [revenue_flipped(x) for x in xs]
    plt.plot(xs, ys)
    plt.plot(current_rate, revenue_flipped(current_rate), 'ro')
    plt.title('Tax Rates and revenue flipped')
    plt.xlabel('Tax Rate')
    plt.ylabel('Revenue')
    print(current_rate)
    plt.show()
    
show_revenue_flipped()