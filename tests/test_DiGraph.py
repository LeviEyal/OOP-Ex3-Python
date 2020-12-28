import unittest
from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphComponents import NodeData


class Test(TestCase):

    def setUp(self) -> None:
        self.g = DiGraph()
        for i in range(6):
            self.g.add_node(i)
        self.g.add_edge(1, 2, 1)
        self.g.add_edge(1, 3, 1)
        self.g.add_edge(1, 4, 1)
        self.g.add_edge(2, 1, 1)
        self.g.add_edge(2, 5, 1)
        self.g.add_edge(3, 1, 1)
        self.g.add_edge(4, 5, 1)
        self.g.add_edge(4, 2, 1)

    # def test_remove_edge(self):
    #     self.assertEqual()

    def test_v_size(self):
        self.assertEqual(6, self.g.v_size())
        # adding a new node:
        self.assertTrue(self.g.add_node(7))
        self.assertEqual(7, self.g.v_size())
        # adding already inside nodes:
        for i in range(6):
            self.assertFalse(self.g.add_node(i))
        self.assertEqual(7, self.g.v_size())
        # adding 3 new nodes (#6, #8, #9):
        for i in range(6, 10):
            self.g.add_node(i)
        self.assertEqual(10, self.g.v_size())

    def test_e_size(self):
        self.assertEqual(8, self.g.e_size())
        # adding old edge - shouldn't update it
        self.assertFalse(self.g.add_edge(1, 2, 3.5))
        self.assertEqual(8, self.g.e_size())

    def test_get_all_v(self):
        d = {0: NodeData(0), 1: NodeData(1), 2: NodeData(2), 3: NodeData(3), 4: NodeData(4), 5: NodeData(5)}
        self.assertEqual(d.__repr__(), self.g.get_all_v().__repr__())

    # def test_all_in_edges_of_node(self):
    #     self.fail()
    #
    # def test_all_out_edges_of_node(self):
    #     self.fail()
    #
    # def test_get_mc(self):
    #     self.fail()
    #
    # def test_add_edge(self):
    #     self.fail()
    #
    # def test_add_node(self):
    #     self.fail()
    #
    # def test_remove_node(self):
    #     self.fail()
    #
    # def test_remove_edge(self):
    #     self.fail()

    if __name__ == '__main__':
        unittest.main()
