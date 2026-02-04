# Problem 1a,b,c 
# NOTE: Problem B and C are to be implemented in this file as well
import matplotlib.pyplot as plt
import networkx as nx


def plan_city_a(num_data_hubs, num_service_providers, connections, provider_capacities, preliminary_assignment) -> bool:
    G = nx.DiGraph()
    pos = {}

    G.add_node("source")
    pos["source"] = (0, num_data_hubs/2)

    for i in range(num_data_hubs):
        G.add_node(f"hub{i}")
        G.add_edge("source",f"hub{i}")
        pos[f"hub{i}"] = (1, (num_data_hubs-i))
    for i in range(num_data_hubs,num_service_providers+num_data_hubs):
        G.add_node(f"prov{i}")
        pos[f"prov{i}"] = (2, (num_data_hubs+num_service_providers)-i)
    
    G.add_node("sink")
    pos["sink"] = (3, num_data_hubs/2)

    for hub, prov in connections.items():
        for p in prov:
            G.add_edge(f"hub{hub}",f"prov{p}")
    
    for index,capacity in enumerate(provider_capacities):
        if capacity>0:
            G.add_edge(f"prov{index}","sink")

    hold_capacities = provider_capacities.copy()
    for hub, prov in preliminary_assignment.items():
        G.remove_edge("source",f"hub{hub}")
        G.add_edge(f"hub{hub}","source")
        G.remove_edge(f"hub{hub}",f"prov{prov}")
        G.add_edge(f"prov{prov}", f"hub{hub}")
        hold_capacities[prov] -= 1
        if hold_capacities[prov] == 0:
            G.remove_edge(f"prov{prov}","sink")
        G.add_edge("sink",f"prov{prov}")

    plt.figure()
    nx.draw(G, pos, with_labels=True, arrows = True,node_size=1000,arrowsize=15, arrowstyle='-|>', node_color="pink")
    plt.show()


    return True


plan_city_a(num_data_hubs = 5 ,
            num_service_providers = 5 ,
            connections = {0: [5 ,7 ,8] , 1: [5 , 8] , 2: [7 ,8 ,9] , 3: [5 , 6 , 8 , 9] , 4: [5 ,6 ,7 ,8]} ,
            provider_capacities = [0]*5 + [0 ,1 ,0 ,2 ,2] ,
            preliminary_assignment = {0: 8 , 1: 8 , 2: 9 , 3: 9})