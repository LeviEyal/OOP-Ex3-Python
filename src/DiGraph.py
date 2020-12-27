import json

from src.GraphInterface import GraphInteface
from src.GraphComponents import NodeData, EdgeData, GeoLocation
import pprint


class DiGraph(GraphInteface):
    """This abstract class represents an interface of a graph."""

    def __init__(self):
        self.V = dict()
        self.Ni_out = dict()
        self.Ni_in = dict()
        self.__nodeSize = 0
        self.__edgeSize = 0
        self.__mc = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.__nodeSize

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.__edgeSize

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair  (key, node_data)
        """
        return self.V

    def all_in_edges_of_node(self, dst: int) -> dict:
        """return a dictionary of all the nodes connected to (into) dst ,
        each node is represented using a pair (key, weight)
         """
        return self.Ni_in.get(dst)

    def all_out_edges_of_node(self, src: int) -> dict:
        """return a dictionary of all the nodes connected from src , each node is represented using a pair (key,
        weight)
        """
        return self.Ni_out.get(src)

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.__mc

    def add_edge(self, src: int, dst: int, w: float) -> bool:
        """
        Adds an edge to the graph.
        @param src: The start node of the edge
        @param dst: The end node of the edge
        @param w: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if src in self.V and dst in self.V and dst not in self.Ni_out[src]:
            e = EdgeData(src, dst, w)
            self.Ni_in[dst][src] = e
            self.Ni_out[src][dst] = e
            self.__mc += 1
            self.__edgeSize += 1
            return True
        return False

    def add_node(self, key: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param key: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if key not in self.V:
            self.V[key] = NodeData(key, location=pos)
            self.Ni_in[key] = {}
            self.Ni_out[key] = {}
            self.__mc += 1
            self.__nodeSize += 1
            return True
        return False

    def remove_node(self, key: int) -> bool:
        """
        Removes a node from the graph.
        @param key: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if key in self.V:
            for k in self.Ni_in.keys():
                if key in self.Ni_in[k].keys():
                    del self.Ni_in[k][key]
            for k in self.Ni_out.keys():
                if key in self.Ni_out[k].keys():
                    del self.Ni_out[k][key]
            self.V.pop(key)
            self.Ni_in.pop(key)
            self.Ni_out.pop(key)
            return True
        return False

    def remove_edge(self, src: int, dst: int) -> bool:
        """
        Removes an edge from the graph.
        @param src: The start node of the edge
        @param dst: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        self.all_out_edges_of_node(src).pop(dst)
        self.all_in_edges_of_node(dst).pop(src)


if __name__ == '__main__':
    g = DiGraph()
    for i in range(6):
        g.add_node(i)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(1, 4, 1)
    g.add_edge(2, 1, 1)
    g.add_edge(2, 5, 1)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 5, 1)
    g.add_edge(4, 2, 1)
    g.add_edge(6, 3, 1)
    g.add_edge(5, 0, 1)
    print(g.Ni_in)
    print(g.Ni_out)
    # g.all_out_edges_of_node(1).pop(2)
    # g.all_in_edges_of_node(2).pop(1)
    # g.remove_edge(1, 2)
    g.remove_node(1)
    print(g.Ni_in)
    print(g.Ni_out)
