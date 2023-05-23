import math, random


def verify_square(square):
    sums = []
    rowsums = [sum(square[i]) for i in range(0, len(square))]
    sums.append(rowsums)
    colsums = [sum([row[i] for row in square]) for i in range(0, len(square))]
    sums.append(colsums)
    main_diag = sum([square[i][i] for i in range(0, len(square))])
    sums.append([main_diag])
    sub_diag = sum([square[i][len(square) - 1 - i]
                   for i in range(0, len(square))])
    sums.append([sub_diag])
    flattened = [j for i in sums for j in i]
    return len(list(set(flattened))) == 1


def rule1(x, n, upright):
    return (x + ((-1) ** upright) * n) % n ** 2


def rule2(x, n, upleft):
    return (x + ((-1) ** upleft)) % n ** 2

def rule3(x, n, upleft):
    return (x + ((-1) ** upleft * (1 - n))) % n ** 2


def pretty_print(square):
    labels = ['['+str(x)+']' for x in range(0, len(square))]
    format_row = '{:>6}' * (len(labels) + 1)
    print(format_row.format("", *labels))
    for label, row in zip(labels, square):
        print(format_row.format(label, *row))


n = 7
center_i = math.floor(n / 2)
center_j = math.floor(n / 2)
entry_i = center_i
entry_j = center_j
directions = ['up_left', 'up_right', 'down_left', 'down_right']
direction = random.choice(directions)

if direction == directions[1]:
    new_entry_i = entry_i - 1
    new_entry_j = entry_j + 1
    square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j], n, True)
    
    
if direction == directions[2]:
    new_entry_i = entry_i + 1
    new_entry_j = entry_j - 1
    square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j], n, False)
    
if direction == directions[0]:
    new_entry_i = entry_i - 1
    new_entry_j = entry_j - 1
    square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j], n, True)
    
    
if direction == directions[3]:
    new_entry_i = entry_i + 1
    new_entry_j = entry_j + 1
    square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j], n, False)

square = [[float('nan') for i in range(0, n)] for j in range(0, n)]
square[center_i][center_j] = int((n**2+1)/2)
square[center_i + 1][center_j] = 1
square[center_i - 1][center_j] = n**2
square[center_i][center_j + 1] = n**2 + 1 - n
square[center_i][center_j - 1] = n

square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
verify_square(square)
pretty_print(square)
