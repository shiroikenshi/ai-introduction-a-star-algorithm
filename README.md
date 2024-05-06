# <div align="center"><a href="/README.md">Português</a> | <a href="/README_EN.md">Inglês</a></div>
<br><br>
# Algoritmo A* no Mapa da Romênia
Este algoritmo implementa o algoritmo A* no mapa da Romênia para encontrar o caminho mais curto entre duas cidades.

### Autor
* Felipe Pinto da Silva

### Classe: Node
Representa um nó no grafo.

#### Atributos
* `name` (str): Nome do nó.
* `parent` (Node, opcional): Nó pai. Padrão: None.
* `distance` (int, opcional): Custo do nó inicial até o nó atual. Padrão: 0.
* `heuristic` (int): Custo estimado do nó atual até o nó de destino.
* `f` (int): Soma do custo e da heurística.

### Função: romania_map()
Define o mapa da Romênia com conexões entre cidades e distâncias.

### Função: heuristic_cost(node_name)
Define uma heurística simples de distância em linha reta (aproximada).

#### Argumentos
* `node_name` (str): Nome do nó atual.

#### Retorna
* `int`: Heurística estimada do nó atual até o nó de destino.

### Função: a_star(graph, start, goal)
Executa o algoritmo A* para encontrar o caminho mais curto de um nó inicial para um nó de destino em um grafo.

#### Argumentos
* `graph` (dict): Grafo representando o mapa.
* `start` (str): Nó inicial.
* `goal` (str): Nó de destino.

#### Retorna
* `list`: Caminho mais curto do nó inicial até o nó de destino.

### Exemplo de Uso
```python
# Define o mapa da Romênia
graph = romania_map()

# Define o ponto de partida e o ponto de chegada
start_point = 'Arad'
end_point = 'Bucharest'

# Executa o algoritmo A* para encontrar o caminho
path = a_star(graph, start_point, end_point)
```

### Exemplo de Saída
```terminal
-| Algoritmo A* |-

Origem: Arad
Destino: Bucharest

Caminho encontrado: ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
```

### Requisitos
* Python 3.x
* Módulo heapq
* Módulo os
