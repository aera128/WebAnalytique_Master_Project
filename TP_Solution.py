import networkx as nx
import itertools
import matplotlib.pyplot as plt
from toolz.itertoolz import last


def get_sample():
    G = nx.Graph()

    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    G.add_edge(5, 6)
    G.add_edge(5, 7)
    G.add_edge(6, 7)

    return G


def load_graph(filename=None, label=None):
    if filename is None:
        return get_sample()
    else:
        return nx.read_gml(filename, label)


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


def community_detection(G, k=1):
    comp = nx.algorithms.community.centrality.girvan_newman(G)
    for communities in itertools.islice(comp, k):
        community = tuple(sorted(c) for c in communities)
    return community


def community_detection_performance(G, k=1):
    comp = nx.algorithms.community.centrality.girvan_newman(G)
    for communities in itertools.islice(comp, k):
        per = nx.algorithms.community.quality.performance(G, communities)
    return per


def plot_community(G, k=1):
    comp = nx.algorithms.community.centrality.girvan_newman(G)
    # k = 1
    for communities in itertools.islice(comp, k):
        for community in communities:
            g = nx.Graph.subgraph(G, community)
            nx.draw(g, with_labels=True)
            plt.show()


def intra_density(G, k=1):
    comp = nx.algorithms.community.centrality.girvan_newman(G)
    # k = 1
    density = []
    for communities in itertools.islice(comp, k):
        for community in communities:
            g = nx.Graph.subgraph(G, community)
            density.append(nx.density(g))
    return density


def inter_density(G, k=1):
    comp = nx.algorithms.community.centrality.girvan_newman(G)
    # k = 1
    density = []
    for communities in itertools.islice(comp, k):
        for community in communities:
            g = nx.Graph.subgraph(G, community)
            inter_edge = 0
            print(community)
            for node in g.nodes:
                edges = G.edges([node])
                for edge in edges:
                    if edge[1] not in g.nodes:
                        # print(edge[1])
                        inter_edge += 1
            possible_edges = (g.number_of_nodes()) * (G.number_of_nodes() - g.number_of_nodes())
            print(inter_edge)
            print(possible_edges)
            density.append(inter_edge / possible_edges)
    return density


def TP1():
    print("SOLUTION OF TP1 STARTS")
    # Exercise A
    G = load_graph()
    # 1 a
    print("Degree Centrality of the sampled Graph ", degree_centrality(G))
    # 1 b
    print("Betweeness Centrality of the sampled Graph ", betweenness_centrality(G))
    # 1 c
    print("Closeness Centrality of the sampled Graph ", closeness_centrality(G))
    # 2
    print("Degree Centrality of the sampled network ", get_graph_degree_centrality(G))
    # 3
    print("Average path length of the sampled Graph ", average_path_length(G))
    # 4
    print("In Degree for the sampled Graph ", in_degree(G))
    print("Out Degree for the sampled Graph ", out_degree(G))
    # 5
    print("Density of the sampled Graph ", graph_density(G))

    # Exerxise B

    dolphin_graph = load_graph('tp1_data.gml')
    # 2
    print("Number of Nodes in Dolphin Network ", dolphin_graph.number_of_nodes())
    print("Number of edges in Dolphin Network ", dolphin_graph.number_of_edges())
    # 3 a
    print("Degree Centrality of the Dolphin Graph ", degree_centrality(dolphin_graph))
    # 3 b
    print("Betweeness Centrality of the Dolphin Graph ", betweenness_centrality(dolphin_graph))
    # 3 c
    print("Closeness Centrality of the Dolphin Graph ", closeness_centrality(dolphin_graph))
    # 4
    print("Degree Centrality of the Dolphin Network ", get_graph_degree_centrality(dolphin_graph))
    # 5
    print("Average path length of the Dolphin Network ", average_path_length(dolphin_graph))
    # 6
    print("In Degree for the Dolphin Network ", in_degree(dolphin_graph))
    print("Out Degree for the Dolphin Network ", out_degree(dolphin_graph))
    # 7
    print("Density of the Dolphin Network ", graph_density(dolphin_graph))
    # 8
    print("Most Popular Dolphin in the Dolphin Network ", most_popular_node(dolphin_graph))


def TP2():
    # 1
    karate_graph = load_graph('./Data2/data2.gml', label='id')
    # # 2 a
    # print("Number of Nodes in Karate Network ", karate_graph.number_of_nodes())
    # print("Number of edges in Karate Network ", karate_graph.number_of_edges())
    # # 2 b
    # print("In Degree for the Karate Network ", in_degree(karate_graph))
    # print("Out Degree for the Karate Network ", out_degree(karate_graph))
    # # 2 c
    # print("Degree Centrality of the Karate Graph ", degree_centrality(karate_graph))
    # # 2 c
    # print("Betweeness Centrality of the Karate Graph ", betweenness_centrality(karate_graph))
    # # 2 c
    # print("Closeness Centrality of the Karate Graph ", closeness_centrality(karate_graph))
    # # 2 c
    # print("Degree Centrality of the Karate Network ", get_graph_degree_centrality(karate_graph))
    # # 2 d
    # print("Density of the Karate Network ", graph_density(karate_graph))
    # # 2 e
    # # print("Average path length of the Karate Network ", average_path_length(karate_graph))
    # # 3 Already Calculted -- Analysis
    # # 4 Already Calculated -- Analysis
    # # 5
    # print("Edge Betweeness Centrality of the Karate Graph ", edge_betweenness_centrality(karate_graph))
    # # 6
    # print("Community Detection ", community_detection(karate_graph))
    # # 7
    # print("Community Detection Performance ", community_detection_performance(karate_graph))
    # # 8 Already Calculated -- Analysis -- In 6 pass the value of k
    # # 9
    # print("Inter Density ", inter_density(karate_graph))
    # # 10
    # print("Intra Density ", intra_density(karate_graph))
    # # 11 Already Calculated -- Analysis -- In 7 pass the value of k
    # # 12 For different number of communities, change the value of k
    # comp = nx.algorithms.community.centrality.girvan_newman(karate_graph)
    # k = 1
    # # print(last(itertools.islice(comp, k)))
    # for community in last(itertools.islice(comp, k)):
    #     print("Community is ", community)
    #     g = nx.Graph.subgraph(karate_graph, community)
    #     print("Most Popular person in the community ", most_popular_node(g))
    # # 13 -- same as above with k = 1
    # comm = tuple(sorted(c) for c in next(comp))
    # for community in comm:
    #     if len(community) == 1:
    #         break
    #     g = nx.Graph.subgraph(karate_graph, community)
    #     print("The id of the teacher is ", most_popular_node(g))
    # 14
    print("Visualization of the whole Network ")
    nx.draw(karate_graph, with_labels=True)
    plt.show()
    # 15
    print("Visualization of the different community")
    plot_community(karate_graph)


# TP1()
TP2()
