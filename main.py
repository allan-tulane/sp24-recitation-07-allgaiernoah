from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        current_node = frontier.pop()
        neighbors = graph[current_node]
        for neighbor in neighbors:
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
    return result





def connected(graph):
    if not graph:  
        return True

    start_node = next(iter(graph)) 
    reachable_nodes = reachable(graph, start_node)
    return len(reachable_nodes) == len(graph)




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    if not graph:
        return 0

    components = 0
    visited = set()
    for node in graph:
        if node not in visited:
            reachable_nodes = reachable(graph, node)
            visited.update(reachable_nodes)
            components += 1
    return components

