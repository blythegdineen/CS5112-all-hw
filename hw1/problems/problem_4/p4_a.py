'''
Problem 4a

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n^2).
'''
def most_frequent_difference_a(values, d_mode) -> int:
    counter = 0
    for i in values:
        for j in values:
            val = i-j
            if val == d_mode:
                counter+=1
    #zero case
    if d_mode == 0:
        counter = counter - len(values)
    return counter

