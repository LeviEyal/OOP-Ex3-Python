from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        self.graph = None
        self.ga = GraphAlgo()

    # def test_get_graph(self):
    #     self.fail()

    def test_load_from_json(self):
        self.ga.load_from_json("../data/A5")
        print(self.ga.get_graph())

    # def test_save_to_json(self):
    #     self.fail()
    #
    # def test_shortest_path(self):
    #     self.fail()
    #
    # def test_connected_component(self):
    #     self.fail()
    #
    # def test_connected_components(self):
    #     self.fail()
    #
    # def test_plot_graph(self):
    #     self.fail()
