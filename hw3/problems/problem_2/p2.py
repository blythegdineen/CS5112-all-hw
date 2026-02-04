# Problem 2

def min_cut(n: int, edge_list: list[tuple[int, int]]) -> int:
    """
    Compute the minimum number of passages (edges) that must be blocked 
    to disconnect Dr. Heinz Doofenshmirtz (at junction 1) from the Tata 
    Innovation Center (at junction n) in a network of junctions.

    The problem is equivalent to finding the minimum cut between node 1 
    and node n in an undirected, unweighted graph.

    Parameters
    ----------
    n : int
        Total number of junctions (1-indexed). 
        Junction 1 represents Doofenshmirtz's studio, and junction n 
        represents the Tata Innovation Center.
        You may assume n ≤ 500.
    
    edge_list : list[tuple[int, int]]
        A list of undirected edges where each tuple (x, y) indicates a 
        two-way passage between junctions x and y. 
        There is at most one passage between any two junctions.

    Returns
    -------
    int
        The minimum number of edges that must be removed to make 
        junction 1 and junction n disconnected.

    Examples
    --------
    >>> min_cut(5, [(1,2), (3,4), (1,5), (2,5)])
    2
    >>> min_cut(12, [(1,4), (1,8), (1,9), (8,9), (9,12), (8,11), (8,12), (3,4), (3,12), (1,5), (2,5)])
    3
    """
    ## build a graph that goes each direction with weights of 1 --> dictionary of dictionaries
    capacity = {i:{} for i in range(1,n+1)}
    for edge in edge_list:
        capacity[edge[0]][edge[1]] = 1
        capacity[edge[1]][edge[0]] = 1

    #BFS 
    def BFS(s, t, paths):
        seen = [False]*(n+1)
        queue = []
        queue.append(s)
        seen[s] = True
        while queue:
            current = queue.pop(0)
            for v in capacity[current]:
                if seen[v] == False and capacity[current][v] > 0:
                    seen[v] = True
                    paths[v] = current

                    queue.append(v)
                    if v == t:
                        return True
        return False
    
    ## FORD FULKERSON
    mincut = 0
    paths = [0]*(n+1)

    while BFS(1, n, paths):
        s = n
        flow = 100

        while(s != 1):
            flow = min(flow, capacity[paths[s]][s])
            s = paths[s] #builds flow backward from sink to source w path found from BFS
        mincut += flow

        #build residual graph
        residual = n
        while(residual != 1):
            prev = paths[residual]
            capacity[prev][residual] -= flow
            capacity[residual][prev] += flow
            residual = prev
    
    return mincut
