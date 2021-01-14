"""
*****************************************************************************
* Eyal Levi ID.203249073
* OOP course 2020 - Ariel University
* Assignment number 4
* https://github.com/LeviEyal
****************************************************************************
"""

import json
import time
from timeit import default_timer as timer
import unittest
from unittest import TestCase

import random
import networkx as nx

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def json_to_nx_graph(file_name):
    try:
        with open(file_name) as f:
            s = json.load(f)
            gt = nx.DiGraph()
        for node in s["Nodes"]:
            gt.add_node(node["id"])

        for edge in s["Edges"]:
            gt.add_edge(edge["src"], edge["dest"], weight=edge["w"])
        return gt
    except Exception as e:
        print(e)
        print("returning None")
        return None
    finally:
        f.close()


def createGraph(nodes: int, edges: int) -> (DiGraph, nx.DiGraph):
    g1 = DiGraph()
    g2 = nx.DiGraph()
    for i in range(nodes):
        g1.add_node(i)
        g2.add_node(i)
    for i in range(edges):
        src = random.randint(0, nodes-1)
        dst = random.randint(0, nodes-1)
        w = random.randint(1, 10)
        g1.add_edge(src, dst, w)
        g2.add_edge(src, dst, weight=w)
    return g1, g2


def compare_shortest_path(g1, g2, k):
    # src = random.randint(0, k)
    # dst = random.randint(0, k)
    src = 3
    dst = 9
    ga = GraphAlgo()
    ga.graph = g1

    start_time = timer()
    print(ga.shortest_path(src, dst)[1])
    ga.shortest_path(src, dst)
    end_time = timer()
    print("My DiGraph time: ", end_time - start_time)

    start_time = timer()
    print(nx.shortest_path(g2, src, dst, weight='weight'))
    # nx.shortest_path(g2, src, dst, weight='weight')
    end_time = timer()
    print("Networkx time: ", end_time - start_time)



def compare_connected_components(g1, g2):
    ga = GraphAlgo()
    ga.graph = g1

    start_time = timer()
    # ga.connected_components()
    print(ga.connected_components())
    end_time = timer()
    print("My DiGraph time: ", end_time - start_time)

    start_time = timer()
    # list(nx.strongly_connected_components(g2))
    print(list(nx.strongly_connected_components(g2)))
    end_time = timer()
    print("Networkx time: ", end_time - start_time)


class Test(TestCase):

    def test_10nodes(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/G_10_80_0.json")
        g1 = ga.get_graph()
        g2 = json_to_nx_graph("../data/G_10_80_0.json")

        print("comparing shortest path:\n")
        compare_shortest_path(g1, g2, 10)

        print("\ncomparing connected components:\n")
        compare_connected_components(g1, g2)

    def test_100nodes(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/G_100_800_0.json")
        g1 = ga.get_graph()
        g2 = json_to_nx_graph("../data/G_100_800_0.json")

        print("comparing shortest path:\n")
        compare_shortest_path(g1, g2, 100)

        print("\ncomparing connected components:\n")
        compare_connected_components(g1, g2)

    def test_1000nodes(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/G_1000_8000_0.json")
        g1 = ga.get_graph()
        g2 = json_to_nx_graph("../data/G_1000_8000_0.json")

        print("comparing shortest path:\n")
        compare_shortest_path(g1, g2, 1000)

        print("\ncomparing connected components:\n")
        compare_connected_components(g1, g2)

    def test_10000nodes(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/G_10000_80000_0.json")
        g1 = ga.get_graph()
        g2 = json_to_nx_graph("../data/G_10000_80000_0.json")

        print("comparing shortest path:\n")
        compare_shortest_path(g1, g2, 10000)

        print("\ncomparing connected components:\n")
        compare_connected_components(g1, g2)

    def test_20000nodes(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/G_20000_160000_0.json")
        g1 = ga.get_graph()
        g2 = json_to_nx_graph("../data/G_20000_160000_0.json")

        print("comparing shortest path:\n")
        compare_shortest_path(g1, g2, 20000)

        print("\ncomparing connected components:\n")
        compare_connected_components(g1, g2)

    def test_30000nodes(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/G_30000_240000_0.json")
        g1 = ga.get_graph()
        g2 = json_to_nx_graph("../data/G_30000_240000_0.json")

        print("comparing shortest path:\n")
        compare_shortest_path(g1, g2, 30000)

        print("\ncomparing connected components:\n")
        compare_connected_components(g1, g2)

    def test_timer(self):
        start_time = timer()
        time.sleep(0.001)
        end_time = timer()
        print("test ", end_time - start_time)

        start_time = time.process_time()
        time.sleep(0.1)
        end_time = time.process_time()
        print("test ", end_time - start_time)

    if __name__ == '__main__':
        unittest.main()

