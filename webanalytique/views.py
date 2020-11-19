import json

import networkx as nx
from django.shortcuts import render

import webanalytique.utils as utils


def index(request):
    return render(request, 'webanalytique/index.html', {})


def data1(request):
    g = nx.read_gml('./Data1/data1.gml', label=None)
    g = g.subgraph(list(g.nodes)[:5000])
    k = 1
    node_links = nx.node_link_data(g)
    comp = nx.algorithms.community.centrality.girvan_newman(g)
    # comp_detect = utils.community_detection(g, comp, 1)
    # print(len(utils.intra_density(g, comp, 1)))
    communities = utils.get_community(g, comp, k)

    return render(request, 'webanalytique/graph.html', {
        "G": json.dumps(node_links),
        "communities_json": json.dumps(communities),
        "communities": communities,
        "comp_perf": utils.community_detection_performance(g, comp, k),
        "nodes": g.nodes,
        "links": g.edges,
        "nodes_number": utils.number_of_nodes(g),
        "links_number": utils.number_of_edges(g),
        "density": utils.graph_density(g),
        "DCN": utils.get_graph_degree_centrality(g),
        "MPN": utils.most_popular_node(g),
        "DC": nx.degree_centrality(g).items(),
        "BC": nx.betweenness_centrality(g).items(),
        "CC": nx.closeness_centrality(g).items(),
    })


def data2(request):
    g = nx.read_gml('./Data2/data2.gml', label=None)
    k = 1
    node_links = nx.node_link_data(g)
    comp = nx.algorithms.community.centrality.girvan_newman(g)
    # comp_detect = utils.community_detection(g, comp, 1)
    # print(len(utils.intra_density(g, comp, 1)))
    communities = utils.get_community(g, comp, k)

    return render(request, 'webanalytique/graph.html', {
        "G": json.dumps(node_links),
        "communities_json": json.dumps(communities),
        "communities": communities,
        "comp_perf": utils.community_detection_performance(g, comp, k),
        "nodes": g.nodes,
        "links": g.edges,
        "nodes_number": utils.number_of_nodes(g),
        "links_number": utils.number_of_edges(g),
        "density": utils.graph_density(g),
        "DCN": utils.get_graph_degree_centrality(g),
        "MPN": utils.most_popular_node(g),
        "DC": nx.degree_centrality(g).items(),
        "BC": nx.betweenness_centrality(g).items(),
        "CC": nx.closeness_centrality(g).items(),
    })
