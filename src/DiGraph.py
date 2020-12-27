import json

from src.GraphInterface import GraphInteface
from src.GraphComponents import NodeData, EdgeData, GeoLocation
import pprint


class DiGraph(GraphInteface):
    """This abstract class represents an interface of a graph."""

    def __init__(self):
        self.V = dict()
        self.E = dict()
        self.Ni = dict()
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

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        return self.E.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """

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
        if self.V[src] is not None:
            self.E[src] = {dst: EdgeData(src, dst, w)}
            self.Ni[src] = {dst: dict()}
            self.__mc += 1
            self.__edgeSize += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        self.V[node_id] = NodeData(node_id, location=pos)
        self.Ni[node_id] = {node_id: dict()}

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """


if __name__ == '__main__':
    # a = dict()
    # src = 5
    # dst = 8
    # w = 3.5
    # a[src] = {dst: EdgeData(src, dst, w)}
    # # a[1][4] = {1: 4}
    # print(a)
    # print(a[src][dst])
    #
    # e = EdgeData(4, 2, 3.4)
    # print(e)
    # # e = EdgeData(2, 3.4)
    # n = NodeData(3)
    # print(n)
    # n = NodeData(3, info="d")
    # print(n)
    # n = NodeData(key=3, tag=4, info="k", location=GeoLocation(3, 5, 2))
    # print(n)
    # n.weight = 3.5
    # # n = NodeData(3)
    # print(n)

    graph = DiGraph()
    graph.add_node(4)
    graph.add_node(19)
    graph.add_node(23)
    graph.add_node(5)
    graph.add_node(1)
    print(graph.get_all_v())
    print(graph.all_in_edges_of_node(1))

    graph.add_edge(4, 1, 1)
    graph.add_edge(1, 4, 3.4)
    graph.add_edge(1, 5, 2.7)
    graph.add_edge(1, 23, 1.4)
    print(graph.all_in_edges_of_node(1))
