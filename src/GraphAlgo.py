import json
from typing import List

from DiGraph import DiGraph
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        """
        @return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            with open(file_name) as f:
                s = json.load(f)
                g = DiGraph()
            for node in s["Nodes"]:
                if "pos" in node:
                    pos = tuple(map(float, str(node["pos"]).split(",")))
                    g.add_node(key=node["id"], position=pos)
                else:
                    g.add_node(key=node["id"])

            for edge in s["Edges"]:
                g.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = g
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            f.close()

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """
        with open('../data/' + file_name, 'w', encoding='utf-8') as f:
            try:
                d = {"Nodes": [], "Edges": []}
                for src in self.graph.Ni_out.keys():
                    for dst, edge in self.graph.all_out_edges_of_node(src).items():
                        d["Edges"].append({"src": src, "w": edge.w, "dest": dst})

                for node in self.graph.V.values():
                    if node.position is not None:
                        d["Nodes"].append({"pos": str(node.position),
                                           "id": node.key})
                    else:
                        d["Nodes"].append({"id": node.key})
                json.dump(d, f, ensure_ascii=False, indent=4)
                return True
            except Exception as e:
                print(e)
                return False
            finally:
                f.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list

        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])

        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
