import random
from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        self.graph = None
        self.ga = GraphAlgo()

    def test_load_from_json(self):
        self.assertTrue(self.ga.load_from_json("../data/A0"))
        print(self.ga.get_graph())
        self.assertTrue(self.ga.load_from_json("../data/A5"))
        print(self.ga.get_graph())
        self.assertTrue(self.ga.load_from_json("../data/A5_edited"))
        print(self.ga.get_graph())
        self.assertTrue(self.ga.load_from_json("../data/T0.json"))
        print(self.ga.get_graph())

    def test_save_to_json(self):
        self.assertTrue(self.ga.load_from_json("../data/A0"))
        self.assertTrue(self.ga.save_to_json("test1.json"))

        self.assertTrue(self.ga.load_from_json("../data/A5"))
        self.assertTrue(self.ga.save_to_json("test2.json"))

        self.assertTrue(self.ga.load_from_json("../data/A5_edited"))
        self.assertTrue(self.ga.save_to_json("test3.json"))

        self.assertTrue(self.ga.load_from_json("../data/T0.json"))
        self.assertTrue(self.ga.save_to_json("test4.json"))

    def test_shortest_path(self):
        g = DiGraph()
        for i in range(10):
            g.add_node(i)
        g.add_edge(1, 2, 0.5)
        g.add_edge(1, 3, 2.5)
        g.add_edge(3, 4, 1.98)
        g.add_edge(2, 5, 8.3)
        g.add_edge(5, 7, 4.1)
        g.add_edge(9, 7, 2.4)
        g.add_edge(6, 7, 3.1)
        g.add_edge(7, 6, 3.1)
        g.add_edge(8, 9, 1.8)
        g.add_edge(4, 9, 9.6)
        g.add_edge(2, 6, 5.6)
        self.ga.graph = g

        self.assertEqual("(15.1, [4, 9, 7, 6])", str(self.ga.shortest_path(4, 6)))
        self.assertEqual("(9.2, [1, 2, 6, 7])", str(self.ga.shortest_path(1, 7)))
        self.assertEqual("(17.080000000000002, [3, 4, 9, 7, 6])", str(self.ga.shortest_path(3, 6)))
        self.assertEqual("(0, [1])", str(self.ga.shortest_path(1, 1)))
        self.assertEqual("(5.6, [2, 6])", str(self.ga.shortest_path(2, 6)))
        self.assertEqual("(12.0, [4, 9, 7])", str(self.ga.shortest_path(4, 7)))
        self.assertIsNone(self.ga.shortest_path(0, 3))
        self.assertIsNone(self.ga.shortest_path(20, 4))
        self.assertIsNone(self.ga.shortest_path(8, 4))
        self.assertIsNone(self.ga.shortest_path(7, 1))
        self.assertIsNone(self.ga.shortest_path(1, 20))

    def test_connected_component(self):
        self.ga.graph = g1
        for j in range(1, 9):
            print(self.ga.connected_component(j))

    def test_connected_components(self):
        self.ga.graph = g1
        sccs = self.ga.connected_components()
        self.assertEqual([[7, 6], [3, 4, 8], [2, 1, 5]], sccs)

    def test_plot_graph(self):
        self.ga.graph = rg
        self.ga.plot_graph()


# ========================== Graph 1 ===========================
g1 = DiGraph()
for i in range(1, 9):
    g1.add_node(i)
g1.add_edge(1, 2, 1)
g1.add_edge(2, 3, 1)
g1.add_edge(3, 4, 1)
g1.add_edge(4, 8, 1)
g1.add_edge(8, 4, 1)
g1.add_edge(4, 3, 1)
g1.add_edge(8, 7, 1)
g1.add_edge(6, 7, 1)
g1.add_edge(7, 6, 1)
g1.add_edge(2, 6, 1)
g1.add_edge(5, 6, 1)
g1.add_edge(2, 5, 1)
g1.add_edge(5, 1, 1)
g1.add_edge(5, 6, 1)

# ========================== Random Graph ===========================
rg = DiGraph()
n = 20
for i in range(n):
    rg.add_node(i)
for i in range(n*3):
    rg.add_edge(random.randint(0, n), random.randint(0, n), random.randint(1, 10))
