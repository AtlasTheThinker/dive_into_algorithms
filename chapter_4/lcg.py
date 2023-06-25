import matplotlib.pyplot as plt

def overlapping_sums(the_list, sum_length):
    length_of_list = len(the_list)
    the_list.extend(the_list)
    output = []
    for n in range(0, length_of_list):
        output.append(sum(the_list[n:(n + sum_length)]))
    return output

def next_random(previous, n1, n2, n3):
    return (previous * n1 + n2) % n3
    
def list_random(n1, n2, n3):
    output = [1]
    while len(output) <= n3:
        output.append(next_random(output[len(output) - 1], n1, n2, n3))
    return output

overlap = overlapping_sums(list_random(211_111, 111_112, 300_007), 22)
plt.hist(overlap, 40, facecolor = 'blue', alpha = 0.5)
plt.title('Result of the Overlapping Sums Test')
plt.xlabel('Sum of Elements of Overlapping Consecutive Sections of List')
plt.ylabel('Frequency of Sum')
plt.show()