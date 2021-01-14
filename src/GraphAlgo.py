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

    def __init__(self, g: DiGraph=DiGraph()):
        self.graph = g

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
        @return: True if the save was successful, False o.w.
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
        @return: The distance of the path, a list of the nodes ids that the path goes through
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
            return None
        path = []
        p = dst
        while p != -1:
            path.insert(0, p)
            p = prev[p]
        return dist[dst], path

    # =========================================================================================
    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        sccs = []
        t = self.graph.keysSet()
        while t:
            scc = self.connected_component(t.pop())
            sccs.append(scc)
            t -= set(scc)
        return sccs

    # =========================================================================================
    def connected_component(self, key: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param key: The node id
        @return: The list of nodes in the SCC
        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        if self.graph is None or key not in self.graph.V.keys():
            return []
        bfs_in = self.BFS(key)
        bfs_out = self.BFS(key, inverted=True)
        return list(bfs_out & bfs_in)

    # =========================================================================================
    def BFS(self, s: int, inverted: bool = False) -> set:
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
                dir_x = (x1 - x2) / math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                dir_y = (y1 - y2) / math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                x1 = dir_x * (-r) + x1
                y1 = dir_y * (-r) + y1
                x2 = dir_x * r + x2
                y2 = dir_y * r + y2

                plt.arrow(x1, y1, (x2 - x1), (y2 - y1),
                          length_includes_head=True, width=0.000003, head_width=0.00015)

        for node in g.get_all_v().values():
            if node.position is None:
                node.position = (random.uniform(0, 5), random.uniform(0, 5), 0)
                # print(node.position)
            plt.plot(node.position[0], node.position[1], 'or', markersize=9, data="d")
            # plt.text(node.position[0], node.position[1], str(node.key))
        plt.show()
