import math

def nested_root(x, length_tolerance):
    output = []
    first_term = math.ceil(x ** 2 / 2)
    the_rest = x * x - first_term
    output.append(first_term)
    while len(output) < length_tolerance:
        first_term = math.ceil(the_rest ** 2 / 2)
        the_rest -= first_term
        output.append(first_term)
    print(output)
    return output

def nested_root_calculate(nested_root):
    index = -1
    output = math.sqrt(nested_root[index])
    index -= 1
    while abs(index) < len(nested_root):
        output += math.sqrt(nested_root[index])
        index -= 1
    return output
        
print(nested_root_calculate(nested_root(3, 10)))