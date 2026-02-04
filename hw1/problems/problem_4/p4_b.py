'''
Problem 4b

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n log n).
'''

def most_frequent_difference_b(values, d_mode) -> int:
    mode_freq = 0

    #1. Sort the list O(nlogn)
    values.sort()
    n = len(values)

    #2. perform binary search for first and last index of complement, returns counts of the complement (last-first)
    def binary_search(complement): 
        # search for first index of complement
        left = 0
        right = n
        while left < right:
            mid = (left+right) //2
            if values[mid] < complement:
                left = mid + 1
            else:
                right = mid
        if left >= n or values[left] != complement: #if no complement found, return 0
            return 0
        first = left   

        #search for last index of complement
        left = 0      
        right = n
        while left < right:
            mid = (left+right) //2
            if values[mid] <= complement:
                left = mid + 1
            else:
                right = mid
        return left - first

    #3. iterate through values
    for val in values:
        complement = val + d_mode
        mode_freq += binary_search(complement)
    
    #zero case
    if d_mode == 0:
        mode_freq = mode_freq - len(values)

    return mode_freq

