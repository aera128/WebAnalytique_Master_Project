import itertools
import json
import os
from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render
import networkx as nx

# Create your views here.
from django.template.defaultfilters import register


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


def community_detection(G, k=1):
    comp = nx.algorithms.community.centrality.girvan_newman(G)
    for communities in itertools.islice(comp, k):
        community = tuple(sorted(c) for c in communities)
    return community


def index(request):
    return render(request, 'webanalytique/index.html', {})


def data1(request):
    print(os.getcwd())
    g = nx.read_gml('./Data1/data1_reduced.gml', label="id")
    node_links = nx.node_link_data(g)
    return render(request, 'webanalytique/graph.html', {
        "G": json.dumps(node_links),
        "nodes": node_links["nodes"],
        "links": node_links["links"],
        "nodes_number": len(node_links["nodes"]),
        "links_number": len(node_links["links"]),
        "density": nx.density(g),
        "DCN": get_graph_degree_centrality(g),
        "DC": nx.degree_centrality(g).items(),
        "BC": nx.betweenness_centrality(g).items(),
        "CC": nx.closeness_centrality(g).items()
    })


def data2(request):
    g = nx.read_gml('../Data2/data2.gml', label="id")
    node_links = nx.node_link_data(g)
    return render(request, 'webanalytique/graph.html', {
        "G": json.dumps(node_links),
        "nodes": node_links["nodes"],
        "links": node_links["links"],
        "nodes_number": len(node_links["nodes"]),
        "links_number": len(node_links["links"]),
        "density": nx.density(g),
        "DCN": get_graph_degree_centrality(g),
        "DC": nx.degree_centrality(g).items(),
        "BC": nx.betweenness_centrality(g).items(),
        "CC": nx.closeness_centrality(g).items()
    })
