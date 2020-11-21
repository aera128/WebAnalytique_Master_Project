from django.shortcuts import render

import webanalytique.utils as utils


def index(request):
    return render(request, 'webanalytique/index.html', {})


def data1(request):
    return render(request, 'webanalytique/graph.html', utils.gen_graph("Data1"))


def data2(request):
    return render(request, 'webanalytique/graph.html', utils.gen_graph("Data2"))
