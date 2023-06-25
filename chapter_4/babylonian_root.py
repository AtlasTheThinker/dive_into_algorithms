import math

def square_root(x, y, error_tolerance):
    error = error_tolerance * 2
    while error > error_tolerance:
        z = x / y
        y = (y + z) / 2
        error = y * y - x
    return y

root = 115
print(square_root(root, 1, 0.1 ** 32) - math.sqrt(root))