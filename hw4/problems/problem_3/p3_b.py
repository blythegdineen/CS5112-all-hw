# Problem 3

def count_min_sketch(a, b, p, w, stream):
    """
    Inputs:
    - a, b: vectors with positive entries
    - p, w: a scalar
    - stream: a list of iterable
    Outputs:
    - a sketch matrix, of size d x w
    """
    out = [[0]*w for _ in range(len(a))]
    ## ((a_i * x + b_i) mod p) mod w 
    for x in stream:
        for i in range(len(a)):
            val = ((a[i]*x + b[i]) % p) % w 
            out[i][val] += 1
    return out 
