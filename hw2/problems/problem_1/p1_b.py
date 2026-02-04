# Problem 1b

def maxsum_tree(vertices, adjacency) -> int:
    num_nodes = len(vertices)
    
    if num_nodes == 0:
        return 0
    if num_nodes == 1:
        return max(0, list(vertices.values())[0])

    all_keys = set(vertices.keys())
    all_children_keys = set()
    for children in adjacency.values():
        all_children_keys.update(children)

    root = (all_keys-all_children_keys).pop()

    include = {}
    exclude = {}

    def include_node(node):
        if node in include:
            return include[node]
        
        node_val = vertices.get(node)
        children = adjacency.get(node)
        maxsum_node = node_val

        if children:
            for child in children:
                maxsum_node += exclude_node(child)
        include[node] = maxsum_node

        return maxsum_node

    def exclude_node(node):
        if node in exclude:
            return exclude[node]
        maxsum_node = 0
        children = adjacency.get(node)
        if children:
            for child in children:
                maxsum_node += max(include_node(child),exclude_node(child))
        exclude[node] = maxsum_node

        return maxsum_node

    return max(include_node(root),exclude_node(root))