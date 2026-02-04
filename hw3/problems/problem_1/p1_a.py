def is_bipartite(g_l):
    # make adjacency list into undirected graph to fix test 5
    undirected = {node:[] for node in g_l}
    for node in g_l:
        for child in g_l[node]:
            undirected[node].append(child)
            if node not in undirected[child]:
                undirected[child].append(node)


    colors = {}
    for node in undirected:
        if node not in colors:
            #BFS
            queue = [node]
            colors[node] = 0
            while queue:
                current = queue.pop(0)
                current_color = colors[current]
                child_color = 1-current_color
                for child in undirected[current]:
                    if child not in colors:
                        colors[child] = child_color
                        queue.append(child)
                    elif colors[child] != child_color:
                        return False
    return True