import json
import math
import random
from typing import List
from queue import PriorityQueue

import matplotlib.pyplot as plt
import numpy as np

from DiGraph import DiGraph
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface

NOT_VISITED = 0
VISITED = 1


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        """
        @return: the directed graph on which the algorithm works on.
        """
        return self.graph

# =========================================================================================
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

# =========================================================================================
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
                    for dst, w in self.graph.all_out_edges_of_node(src).items():
                        d["Edges"].append({"src": src, "w": w, "dest": dst})

                for node in self.graph.V.values():
                    if node.position is not None:
                        d["Nodes"].append({"pos": str(node.position), "id": node.key})
                    else:
                        d["Nodes"].append({"id": node.key})
                json.dump(d, f, ensure_ascii=False, indent=4)
                return True
            except Exception as e:
                print("Error save to Json: " + e.__repr__())
                return False
            finally:
                f.close()

# =========================================================================================
    def shortest_path(self, src: int, dst: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param src: The start node id
        @param dst: The end node id
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
        nodes = self.graph.get_all_v()
        if src not in nodes or dst not in nodes:
            return None

        prev = {src: -1}
        q = PriorityQueue()
        q.put(nodes[src])
        self.set_all_nodes(math.inf)

        nodes[src].tag = 0
        while not q.empty():
            v = q.get()
            for k, w in self.graph.all_out_edges_of_node(v.key).items():
                n = nodes[k]
                weight_from_src = v.tag + w
                if weight_from_src < n.tag:
                    q.put(n)
                    n.tag = weight_from_src
                    prev[n.key] = v.key
        if nodes[dst].tag == math.inf:
            return None
        path = []
        p = dst
        while p != -1:
            path.append(nodes[p])
            p = prev[p]
        path.reverse()
        return nodes[dst].tag, path

# =========================================================================================
    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        visited = []
        ans = []
        for n in self.graph.V.keys():
            if n not in visited:
                scc = self.connected_component(n)
                visited.extend(scc)
                ans.append(scc)
        return ans

# =========================================================================================
    def connected_component(self, key: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param key: The node id
        @return: The list of nodes in the SCC
        """
        bfs_out = self.BFS(key, False)
        bfs_in = self.BFS(key, True)
        return list(set(bfs_out) & set(bfs_in))

# =========================================================================================
    def BFS(self, s: int, flag: bool) -> list:
        visited = {i: False for i in self.graph.V.keys()}
        visited[s] = True
        queue = [s]
        t = [s]
        while queue:
            current = queue.pop()
            if flag:
                p = self.graph.all_out_edges_of_node(current).keys()
            else:
                p = self.graph.all_in_edges_of_node(current).keys()

            for u in p:
                if not visited[u]:
                    visited[u] = True
                    queue.append(u)
                    t.append(u)
        return t

# =========================================================================================
    def set_all_nodes(self, t):
        for n in self.graph.get_all_v().values():
            n.tag = t

# =========================================================================================
    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        g = self.get_graph()
        for key in g.get_all_v().keys():
            for k, w in g.all_out_edges_of_node(key).items():
                r = 0.0001
                x1 = g.get_node(key).position[0]
                y1 = g.get_node(key).position[1]
                x2 = g.get_node(k).position[0]
                y2 = g.get_node(k).position[1]
                # print(x1,x2,y1,y2)
                dir_x = (x1-x2)/math.sqrt((x1-x2)**2 + (y1-y2)**2)
                dir_y = (y1-y2)/math.sqrt((x1-x2)**2 + (y1-y2)**2)
                x1 = dir_x*(-r) + x1
                y1 = dir_y*(-r) + y1
                x2 = dir_x*r + x2
                y2 = dir_y*r + y2

                plt.arrow(x1, y1, (x2-x1), (y2-y1),
                          length_includes_head=True, width=0.000003, head_width=0.00015)

        for node in g.get_all_v().values():
            if node.position is None:
                node.position = (random.uniform(0, 5), random.uniform(0, 5), 0)
                # print(node.position)
            plt.plot(node.position[0], node.position[1], 'or', markersize=9, data="d")
            # plt.text(node.position[0], node.position[1], str(node.key))
        plt.show()
