# Problem 3b — 2-opt Local Search
#
# Implement local_search_2opt(c, init) as specified in the HW3 PDF.
# - c: n x n symmetric cost matrix (float('inf') on diagonal)
# - init: a tuple or list representing a permutation of 1..n (1-based labels)
# Return:
# - an improved permutation (as a tuple) obtained by repeatedly applying 2-opt
#   until no improving swap exists.
#
# Notes:
# - cost(s) = sum_{i=1..n-1} c[s[i]][s[i+1]] with 1-based gene labels
# - 2-opt(i,j) reverses the subsequence s[i..j] (0-based positions)
# - Only accept a swap if it strictly improves total path cost.

def local_search_2opt(cost_matrix, init):
    """
    Perform 2-opt local search on a path (not a cycle).

    Args:
        cost_matrix: list[list[float]] of shape n x n, symmetric, c[i][i] = inf
        init: sequence (list/tuple) of 1..n (1-based labels)

    Returns:
        tuple: locally optimal permutation under 2-opt.
    """
    best_cost = 0
    best_list = list(init)

    for i in range(len(init)-1):
        best_cost += cost_matrix[init[i]-1][init[i+1]-1]
    
    improved_found = True
    iteration = 0
    
    while improved_found:
        iteration +=1
        improved_found = False
        best_swap = None
        best_swap_cost = best_cost
        for i in range(len(best_list)):
            for j in range(i+1, len(best_list)):
                swapping = best_list.copy()
                temp_cost = 0
                swapping[i], swapping[j] = swapping[j], swapping[i]
                for q in range(len(swapping)-1):
                    temp_cost += cost_matrix[swapping[q]-1][swapping[q+1]-1]
                if temp_cost < best_swap_cost:
                    best_swap_cost = temp_cost
                    best_swap = swapping
                    improved_found = True
        
        if improved_found:
            best_cost = best_swap_cost
            best_list = best_swap
    return tuple(best_list)