'''
Problem 4c

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n).
'''
def most_frequent_difference_c(values, d_mode) -> int:
    mode_freq = 0
    # 1. count frequencies of val in values
    freqs = {}
    for i in values:
        if i in freqs:
            freqs[i] +=1
        else:
            freqs[i] = 1

    # 2. for each unique val, check if val + d_mode in list
    for val in set(values):
        diff = val + d_mode
        if diff in values: 
            # 3. if above true, then count number of times it occurs (freq val * freq val+dmode)
            mode_freq += freqs[val] * freqs[diff]
    
    if d_mode == 0:
        mode_freq = mode_freq - len(values)

    return mode_freq