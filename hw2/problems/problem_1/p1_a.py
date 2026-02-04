# Problem 1a

def maxsum_list(xs) -> int:
    length_xs = len(xs)
    
    if length_xs==0:
        return 0
    if length_xs ==1:
        return max(0,xs[0])
    
    # calculate maxsum i without recursion
    i_minus_two = 0            #length_xs = 0
    i_minus_one = max(0,xs[0]) #length_xs = 1
    i_maxsum = 0 

    # iterate through all items in the list
    for i in range(1,length_xs):
        i_maxsum = max(i_minus_one, i_minus_two+ xs[i])
        i_minus_two = i_minus_one
        i_minus_one = i_maxsum

    return i_maxsum

    ## Works but is too slow:

    # maxsum_minus_one = maxsum_list(xs[:(length_xs-1)])
    # maxsum_minus_two = maxsum_list(xs[:(length_xs-2)])

    # return max(maxsum_minus_one, maxsum_minus_two+xs[length_xs-1])