"""
*****************************************************************************
* Eyal Levi ID.203249073
* OOP course 2020 - Ariel University
* Assignment number 4
* https://github.com/LeviEyal
****************************************************************************
"""

import heapq
import json
import math
import random
from typing import List

import matplotlib.pyplot as plt

from DiGraph import DiGraph
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = DiGraph()):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    # -----------------------------------------------------------------------------------------
    # ******************************** Load graph from json ***********************************
    # -----------------------------------------------------------------------------------------
    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        :param file_name: The path to the json file
        :returns True if the loading was successful, False o.w.
        """
        try:
            with open(file_name) as f:
                s = json.load(f)
                g = DiGraph()
            for node in s["Nodes"]:
                if "pos" in node:
                    pos = tuple(map(float, str(node["pos"]).split(",")))
                else:
                    pos = None
                g.add_node(key=node["id"], pos=pos)

            for edge in s["Edges"]:
                g.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = g
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            f.close()

    # -----------------------------------------------------------------------------------------
    # ********************************* Save graph to json ************************************
    # -----------------------------------------------------------------------------------------
    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        :param file_name: The path to the out file
        :return: True if the save was successful, False o.w.
        """
        with open('../data/' + file_name, 'w', encoding='utf-8') as f:
            try:
                d = {"Nodes": [], "Edges": []}
                for src in self.graph.Ni_out.keys():
                    for dst, w in self.graph.all_out_edges_of_node(src).items():
                        d["Edges"].append({"src": src, "w": w, "dest": dst})

                for node in self.graph.V.values():
                    if node.pos is not None:
                        t = "{}, {}, {}".format(node.pos[0], node.pos[1], node.pos[2])
                        d["Nodes"].append({"pos": t, "id": node.key})
                    else:
                        d["Nodes"].append({"id": node.key})
                json.dump(d, f, ensure_ascii=False, indent=4)
                return True
            except Exception as e:
                print("Error save to Json: " + e.__repr__())
                return False
            finally:
                f.close()

    # -----------------------------------------------------------------------------------------
    # *********************************** Shortest path ***************************************
    # -----------------------------------------------------------------------------------------

    def shortest_path(self, src: int, dst: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        :param src: The start node id
        :param dst: The end node id
        :return: The distance of the path, a list of the nodes ids that the path goes through
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm

        """
        # ------------------ Pre checks: ------------------- #
        nodes = self.graph.get_all_v()
        if src not in nodes or dst not in nodes:
            return None

        # ----------------- Dijkstra core: ----------------- #
        prev = {src: -1}
        dist = {i: math.inf for i in nodes.keys()}
        dist[src] = 0
        q = []
        heapq.heappush(q, (0, src))
        while q:
            v = heapq.heappop(q)[1]
            for u, w in self.graph.all_out_edges_of_node(v).items():
                if dist[u] > dist[v] + w:
                    dist[u] = dist[v] + w
                    prev[u] = v
                    heapq.heappush(q, (dist[u], u))
            if v == dst:
                break

        # -------------- Retrieving the path: -------------- #
        if dist[dst] == math.inf:
            return math.inf, []
        path = []
        p = dst
        while p != -1:
            path.insert(0, p)
            p = prev[p]
        return dist[dst], path

    # -----------------------------------------------------------------------------------------
    # ******************************** Connected components ***********************************
    # -----------------------------------------------------------------------------------------
    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
            1. hold a list containing all the graph's nodes keys
            2. for each node in the list find its Strongly Connected Component(SCC)
            3. remove the SCC members from the list
            4. repeat till the list is empty
        :return: The list all SCC
        """
        sccs = []
        t = self.graph.keysSet()
        while t:
            scc = self.connected_component(t.pop())
            sccs.append(scc)
            t -= set(scc)
        return sccs

    # -----------------------------------------------------------------------------------------
    # ******************************** Connected component ************************************
    # -----------------------------------------------------------------------------------------
    def connected_component(self, key: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
            1. run BFS on the graph from the given node, and store the visited nodes in bfs_in
            2. run BFS on the Transposed graph from the given node, and store the visited nodes in bfs_out
            3. the intersection of bfs_in and bfs_out is the strongly connected component of the given node.

        :param key: The node id
        :return: The list of nodes in the SCC
        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        if self.graph is None or key not in self.graph.V.keys():
            return []
        bfs_in = self.BFS(key)
        bfs_out = self.BFS(key, inverted=True)
        return list(bfs_out & bfs_in)

    # =========================================================================
    def BFS(self, s: int, inverted: bool = False) -> set:
        """
        Traverse the graph using BFS algorithm
        :param s: the starting vertex
        :param inverted: if True, traverse the transposed graph
        :return: a set of all vertices the been visited during the BFS travers
        """
        q = [s]
        visited = {s}
        while q:
            v = q.pop()
            v_adjs = self.graph.all_out_edges_of_node(v).keys() if inverted \
                else self.graph.all_in_edges_of_node(v).keys()

            for u in v_adjs:
                if u not in visited:
                    q.append(u)
                    visited.add(u)
        return visited

    # -----------------------------------------------------------------------------------------
    # *********************************** Graph plotting **************************************
    # -----------------------------------------------------------------------------------------
    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in random positions.
        :return: None
        """
        g = self.get_graph()
        for src in g.get_all_v().keys():
            for dst, w in g.all_out_edges_of_node(src).items():
                r = 0.0002
                x1, y1, z1 = g.get_node(src).pos
                x2, y2, z2 = g.get_node(dst).pos
                distp1p2 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if distp1p2 == 0:
                    distp1p2 = 1
                dir_x = (x1 - x2) / distp1p2
                dir_y = (y1 - y2) / distp1p2
                x1 = dir_x * (-r) + x1
                y1 = dir_y * (-r) + y1
                x2 = dir_x * r + x2
                y2 = dir_y * r + y2

                plt.arrow(x1, y1, (x2 - x1), (y2 - y1),
                          length_includes_head=True, width=0.003 * distp1p2, head_width=0.1 * distp1p2, color='black')

        for node in g.get_all_v().values():
            if node.pos is None:
                node.pos = (random.uniform(0, 5), random.uniform(0, 5), 0)
            plt.text(node.pos[0], node.pos[1], str(node.key), horizontalalignment='center',
                     verticalalignment='center',
                     bbox=dict(facecolor='red', edgecolor='black', boxstyle='circle, pad=0.1'))
        plt.show()
