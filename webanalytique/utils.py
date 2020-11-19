import itertools

import networkx as nx


def number_of_nodes(graph):
    return len(graph.nodes)


def number_of_edges(graph):
    return len(graph.edges)


def degree_centrality(graph):
    return nx.degree_centrality(graph)


def betweenness_centrality(graph):
    return nx.betweenness_centrality(graph)


def closeness_centrality(graph):
    return nx.closeness_centrality(graph)


def get_graph_degree_centrality(graph):
    degrees = list(graph.degree)
    list_degree = []
    for i in range(len(degrees)):
        list_degree.append(degrees[i][1])
    max_degree = max(list_degree)
    tmp = 0
    for i in range(len(degrees)):
        tmp += (max_degree - degrees[i][1])
    graph_centrality = tmp / ((len(degrees) - 1) * (len(degrees) - 2))
    return graph_centrality


def most_popular_node(graph):
    degrees = list(graph.degree)
    node = degrees[0]
    for i in range(len(degrees)):
        if degrees[i][1] > node[1]:
            node = degrees[i]
    return node


def in_degree(graph):
    if nx.is_directed(graph):
        return graph.in_degree
    else:
        return graph.degree


def out_degree(graph):
    if nx.is_directed(graph):
        return graph.out_degree
    else:
        return graph.degree


def graph_density(graph):
    return nx.density(graph)


def average_path_length(graph):
    return nx.average_shortest_path_length(graph)


def edge_betweenness_centrality(graph):
    return nx.edge_betweenness_centrality(graph)


def community_detection(G, comp, k=1):
    for communities in itertools.islice(comp, k):
        community = tuple(sorted(c) for c in communities)
    return community


def community_detection_performance(G, comp, k=1):
    for communities in itertools.islice(comp, k):
        per = nx.algorithms.community.quality.performance(G, communities)
    return per


def get_community(G, comp, k=1):
    comp_list = list()
    i = 0
    # k = 1
    for communities in itertools.islice(comp, k):
        for community in communities:
            g = nx.Graph.subgraph(G, community)
            intra_density = nx.density(g)
            inter_edge = 0
            for node in g.nodes:
                edges = G.edges([node])
                for edge in edges:
                    if edge[1] not in g.nodes:
                        # print(edge[1])
                        inter_edge += 1
            possible_edges = (g.number_of_nodes()) * (G.number_of_nodes() - g.number_of_nodes())
            inter_density = inter_edge / possible_edges
            comp_list.append({
                "id": i,
                "graph": nx.node_link_data(g),
                "nb_nodes": len(g.nodes),
                "nb_edges": len(g.edges),
                "intra_density": intra_density,
                "inter_density": inter_density
            })
            i += 1
    return comp_list
