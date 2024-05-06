# <div align="center"><a href="/README.md">Portuguese</a> | <a href="/README_EN.md">English</a></div>
<br><br>
# A* Algorithm on the Romania Map
This algorithm implements the A* algorithm on the map of Romania to find the shortest path between two cities.

### Author
* Felipe Pinto da Silva

### Class: Node
Represents a node in the graph.

#### Attributes
* `name` (str): Name of the node.
* `parent` (Node, optional): Parent node. Defaults to None.
* `distance` (int, optional): Cost from the start node to the current node. Defaults to 0.
* `heuristic` (int): Estimated cost from the current node to the destination node.
* `f` (int): Sum of the cost and heuristic.

### Function: romania_map()
Defines the map of Romania with connections between cities and distances.

### Function: heuristic_cost(node_name)
Defines a simple heuristic of straight-line distance (approximated).

#### Arguments
* `node_name` (str): Name of the current node.

#### Returns
* `int`: Estimated heuristic from the current node to the destination node.

### Function: a_star(graph, start, goal)
Executes the A* algorithm to find the shortest path from a start node to a goal node in a graph.

#### Arguments
* `graph` (dict): Graph representing the map.
* `start` (str): Start node.
* `goal` (str): Destination node.

#### Returns
* `list`: Shortest path from the start node to the destination node.

## Example Usage
```python
# Define the map of Romania
graph = romania_map()

# Define the start and end points
start_point = 'Arad'
end_point = 'Bucharest'

# Execute the A* algorithm to find the path
path = a_star(graph, start_point, end_point)
```

### Output Example
```terminal
-| Algoritmo A* |-

Origem: Arad
Destino: Bucharest

Caminho encontrado: ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
```

### Requirements
* Python 3.x
* Módulo heapq
* Módulo os
