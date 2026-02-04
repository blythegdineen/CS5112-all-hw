# Problem 1e

def plan_city_e(num_data_hubs, num_service_providers, connections, provider_capacities, preliminary_assignment):
    ## build graph
    capacity = {}
    def add_edge(u,v,cap, graph):
        if u not in graph:
            graph[u] = {}
        graph[u][v] = cap
    
    for i in range(num_data_hubs):
        add_edge("source",f"hub{i}",1, capacity)
    for hub, prov in connections.items():
        for p in prov:
            add_edge(f"hub{hub}",f"prov{p}",1, capacity)
    for index,cap in enumerate(provider_capacities):
        if cap>0:
            add_edge(f"prov{index}","sink",cap, capacity)

    ## build residual graph
    residual = {u: {v:cap for v, cap in neighbors.items()} for u, neighbors in capacity.items()}
    
    for hub, prov in preliminary_assignment.items():
        residual["source"][f"hub{hub}"] = 0
        add_edge(f"hub{hub}","source",1, residual)
        residual[f"hub{hub}"][f"prov{prov}"] = 0
        add_edge(f"prov{prov}", f"hub{hub}",1, residual)
        residual[f"prov{prov}"]["sink"] -= 1
        if "sink" not in residual:
            residual["sink"] = {}
        if f"prov{prov}" not in residual["sink"]:
            residual["sink"][f"prov{prov}"] = 0
        residual["sink"][f"prov{prov}"] += 1


    ## BFS to find augmenting path
    def BFS(source, sink, paths):
        visited = set()
        queue = [source]
        visited.add(source)
        while queue:
            current = queue.pop(0)
            if current not in residual:
                continue
            for v in residual[current]:
                if v not in visited and residual[current][v] > 0:
                    visited.add(v)
                    paths[v] = current
                    queue.append(v)
                    if v == sink:
                        return True
        return False
    
    ## FORD FULKERSON
    max_flow = 0
    paths = {}
    # final_hub_path = []

    while BFS("source", "sink", paths):
        s = "sink"
        flow = float("inf")

        while(s != "source"):
            flow = min(flow, residual[paths[s]][s])
            s = paths[s] 
        max_flow += flow

        v = "sink"
        while(v != "source"):
            prev = paths[v]
            residual[prev][v] -= flow
            if v not in residual:
                residual[v] = {}
            if prev not in residual[v]:
                residual[v][prev] = 0
            residual[v][prev] += flow
            v = paths[v]

        paths = {}
    
    n = num_data_hubs - 1
    if max_flow >= 1:
        #return assignment list
        assignments = [0]* num_data_hubs
        for hub, prov in preliminary_assignment.items():
            assignments[hub] = prov

        #use residual graph to find assignment for final hub
        for p in connections[n]:
            if f"prov{p}" in residual and f"hub{n}" in residual[f"prov{p}"] and residual[f"prov{p}"][f"hub{n}"]>0:
                assignments[n] = p
    else:
        assignments = [0]* (num_data_hubs + num_service_providers)
        for p in connections[n]:
            if f"prov{p}" in residual and "sink" in residual[f"prov{p}"] and residual[f"prov{p}"]["sink"] == 0:
                residual[f"prov{p}"]["sink"] = 1
                if BFS("source", "sink", paths):
                    assignments[p] = 1
                residual[f"prov{p}"]["sink"] = 0

    return assignments