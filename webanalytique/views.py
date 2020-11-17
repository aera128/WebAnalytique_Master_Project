import json
from pprint import pprint

from django.shortcuts import render
import networkx as nx

# Create your views here.
from django.template.defaultfilters import register


def index(request):
    return render(request, 'webanalytique/index.html', {})


def data1(request):
    g = nx.read_gml('../Data2/data2.gml', label="id")
    node_links = nx.node_link_data(g)
    return render(request, 'webanalytique/data1.html', {
        "G": json.dumps(node_links),
        "nodes": node_links["nodes"],
        "links": node_links["links"],
        "nodes_number": len(node_links["nodes"]),
        "links_number": len(node_links["links"]),
        "density": nx.density(g),
        "DC": nx.degree_centrality(g).items(),
        "BC": nx.betweenness_centrality(g).items(),
        "CC": nx.closeness_centrality(g).items()
    })


def data2(request):
    return render(request, 'webanalytique/data2.html', {})
