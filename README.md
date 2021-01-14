# OOP-Ex3-Python
מטלה רביעית ואחרונה בקורס תכנות מונחה עצמים - סמסטר א' תשפ"א דצמבר 2020

## About the project
This project is an implementation of a weighted directed graph accompanied by 
different graphs algorithms implemented in Python. 
A graph is represented in adjacency list and and each one contains a list of vertices and a list of weithed edges.

# The graph representation
The graph represented by adjacency list and in particular with 3 dictionaries:
- vertices dictionary
- "out-edges" dictionary {src: {dst1:w1, dst2:w2...} , ...}
- "in-edges" dictionary {dst: {src1:w1, src2:w2...} , ...}

for example the following graph:<br>
<img src="https://user-images.githubusercontent.com/48846533/104158293-af6a3c00-53f5-11eb-9874-90bbd8f9df80.png" alt="drawing" width="400"/>

would be represented:

#### vertices dictionary:
```
{
    0: NodeData#0,
    1: NodeData#1,
    2: NodeData#2,
    3: NodeData#3,
    4: NodeData#4
}
```
#### out edges dictionary:
```
{
    0: {1: 3, 3: 7, 4: 8},
    1: {2: 1, 3: 4},
    2: {},
    3: {2: 2},
    4: {3: 3},
    5: {}
}
```

#### in edges dictionary:

```
{
    0: {},
    1: {0: 3},
    2: {1: 1, 3: 2},
    3: {0: 7, 1: 4, 4: 3},
    4: {0: 8}
}
```

# DiGraph class summary
| Method  | Description  | Complexity |
| :------ |:-------------| :---------:|
| .add_node(key, position)| adds a vertex to the graph. | O(1) |
| .remove_node(key)| removes a vertex with all its edges from the graph by its key|O(E)|
|.get_node()|returns the vertex associated with a given key|O(1)|
|.addEdge(srcKey, destKey, weight)|adds an edge with a weight between two existing vertices. The edge is a direction from source to destination when added in a directed graph. If the edge already exists or one of the nodes dose not exists the functions will do nothing|O(1)|
|.removeEdge(srcKey, destKey)|removes an edge between two existing vertices|O(1)|
|.all_in_edges_of_node(dstKey)|return a dictionary of all the nodes connected to (into) dst , each node is represented using a pair (key, weight)|O(1)|
|.all_out_edges_of_node(srcKey)|return a dictionary of all the nodes connected from src , each node is represented using a pair (key, weight)|O(1)|
|.v_size()|gets the number of vertices in the graph.|O(1)|
|.e_size()|gets the number of edges in the graph.|O(1)|
|.get_mc()|Returns the current version of this graph, on every change in the graph state - the MC should be increased|O(1)|
|.repr()|Returns a string representation of the graph|O(V+E)|


# GraphAlgo class summary
| Method  | Description  | Complexity |
| :------ |:-------------| :---------:|
|.load_from_json(file_name)|Loads a graph from a json file.|O(V+E)|
|.save_to_json(file_name)|Saves the graph in JSON format to a file|O(V+E)|
|.shortest_path(src, dst)|Returns the shortest path from node src to node dst using Dijkstra's Algorithm|O(V+E)|
|.connected_component(key)|Finds the Strongly Connected Component(SCC) that node id1 is a part of.|O(V+E)|
|.connected_components()|Finds all the Strongly Connected Component(SCC) in the graph.|O(V*(V+E))|
|.plot_graph()|Plots the graph. If the nodes have a position, the nodes will be placed there. Otherwise, they will be placed in a random|O(V+E)|

# Graph plotting examples
<img src="https://user-images.githubusercontent.com/48846533/104601238-a80b9280-5682-11eb-874f-ff61cf4d89ef.png" alt="drawing" width="400"/>
<img src="https://user-images.githubusercontent.com/48846533/104601248-ac37b000-5682-11eb-8a99-0299e618933f.png" alt="drawing" width="400"/>
