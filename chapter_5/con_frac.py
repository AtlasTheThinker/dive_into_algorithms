import math

def continued_fraction_decimal(x, error_tolerance, length_tolerance):
    output = []
    first_term = int(x)
    the_rest = x - first_term
    error = the_rest
    output.append(first_term)
    while len(output) < length_tolerance:
        next_term = math.floor(1 / the_rest)
        output.append(next_term)
        the_rest = 1 / the_rest - next_term
        error = abs(get_number(output) - x)
    return output

def continued_fraction(x, y, length_tolerance):
    nom = max(x,y)
    denom = min(x,y)
    output = []
    while denom > 0 and len(output) < length_tolerance:
        whole_part = math.floor(nom / denom)
        output.append(whole_part)
        new_denom = nom % denom
        nom = denom
        denom = new_denom
    return output

def get_number(continued_fraction):
    index = -1
    number = continued_fraction[index]
    
    while abs(index) < len(continued_fraction):
        next = continued_fraction[index - 1]
        number = 1 / number + next
        index -= 1
    return number
        

print(continued_fraction_decimal(1.4142135623730951, 0.1, 1000))