"""
Algoritmo A* implementado no mapa da Romênia

Autores:
    Felipe Pinto da Silva    - 26533952
    Camila Ferreira de Sousa - 28396073
    Hugo Nascimento Pedro    - 26370174
"""
import heapq # Manipular lista
import os # Limpar terminal

class Node:
    def __init__(self, name, parent=None, distance=0):
        """
        Classe que representa um nó no grafo.

        Args:
            name (str): Nome do nó.
            parent (Node, optional): Nó pai. Defaults to None.
            distance (int, optional): Custo do ponto inicial ao ponto atual. Defaults to 0.
        """
        self.name = name
        self.parent = parent
        self.distance = distance  # custo do ponto inicial ao ponto atual
        self.heuristic = 0  # custo estimado do ponto atual ao ponto de destino
        self.f = 0  # soma dos custos e heurística

    def __eq__(self, other):
        """
        Quando utilizado o operador de igualdade entre dois objetos.

        Verifica se dois nós são iguais.

        Args:
            other (Node): Outro nó a ser comparado.

        Returns:
            bool: True se os nós são iguais, False caso contrário.
        """
        return self.name == other.name

    def __lt__(self, other):
        """
        Quando utilizado o operador de menor ou menor ou igual entre dois objetos.

        Verifica se o custo total deste nó é menor que o custo total de outro nó.

        Args:
            other (Node): Outro nó a ser comparado.

        Returns:
            bool: True se o custo total deste nó é menor, False caso contrário.
        """
        return self.f < other.f

def romania_map():
    """
    Define o mapa da Romênia com as conexões entre as cidades e as distâncias.

    Returns:
        dict: Um dicionário representando o grafo.
    """
    graph = {
        'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
        'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu Vilcea': 80},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Zerind': {'Arad': 75, 'Oradea': 71},
        'Oradea': {'Sibiu': 151, 'Zerind': 71},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
        'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
        'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
        'Drobeta': {'Mehadia': 75, 'Craiova': 120},
        'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
        'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
        'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
        'Giurgiu': {'Bucharest': 90},
        'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
        'Hirsova': {'Urziceni': 98, 'Eforie': 86},
        'Eforie': {'Hirsova': 86},
        'Vaslui': {'Urziceni': 142, 'Iasi': 92},
        'Iasi': {'Vaslui': 92, 'Neamt': 87},
        'Neamt': {'Iasi': 87}
    }
    return graph

def heuristic_cost(node_name):
    """
    Define uma heurística simples de distância em linha reta (aproximada).

    Args:
        node_name (str): Nome do nó atual.

    Returns:
        int: Heurística estimada do ponto atual ao ponto de destino.
    """
    heuristic_values = {
        'Arad': 366,
        'Bucharest': 0,
        'Craiova': 160,
        'Drobeta': 242,
        'Eforie': 161,
        'Fagaras': 178,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 380,
        'Pitesti': 98,
        'Rimnicu Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374
    }
    return heuristic_values[node_name]

def a_star(graph, start, goal):
    """
    Executa o algoritmo A* para encontrar o caminho mais curto de um nó inicial para um nó de destino em um grafo.

    Args:
        graph (dict): O grafo que representa o mapa.
        start (str): O nó inicial.
        goal (str): O nó de destino.

    Returns:
        list: O caminho mais curto do nó inicial ao nó de destino.
    """
    # Inicializa os nós de início e fim
    start_node = Node(start)
    goal_node = Node(goal)

    # Inicializa as listas aberta e fechada
    open_list = []
    closed_list = []

    # Adiciona o nó de início à lista aberta
    heapq.heappush(open_list, (start_node.f, start_node))

    # Loop principal do algoritmo A*
    while open_list:
        # Obtém o nó atual da lista aberta
        current_node = heapq.heappop(open_list)[1]

        # Adiciona o nó atual à lista fechada
        closed_list.append(current_node)

        # Verifica se alcançamos o nó de destino
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Retorna o caminho do fim ao início

        # Gera os nós filhos
        children = []
        for neighbor, distance in graph[current_node.name].items():
            # Define o vizinho de current_node como nó filho
            child_node = Node(neighbor, current_node, distance)
            # Cálculo do custo real (g(n)), somasse o custo do nó atual ao custo da aresta que leva ao nó filho
            child_node.distance = current_node.distance + distance
            # Cálculo do custo heurístico (h(n)), retorna uma heurística simples de distância em linha reta do nó atual ao nó destino
            child_node.heuristic = heuristic_cost(neighbor)
            # Cálculo do custo total (f(n)), é calculando somando os dois valores anteriores, g(n) e h(n)
            child_node.f = child_node.distance + child_node.heuristic # f(n) = g(n) + h(n)
            children.append(child_node)

        # Loop através dos nós filhos
        for child in children:
            # Verifica se o filho está na lista fechada
            if any(child == closed_node for closed_node in closed_list):
                continue

            # Verifica se o filho está na lista aberta e se é melhor que o existente
            for open_node in open_list:
                if child == open_node[1] and child.f > open_node[1].f:
                    break
            else:
                # Adiciona o filho à lista aberta
                heapq.heappush(open_list, (child.f, child))

    return None  # Retorna None se não houver caminho encontrado

# Exemplo de uso
if __name__ == "__main__":
    # Define o mapa da Romênia
    graph = romania_map()
    
    # Define o ponto de partida e o ponto de chegada
    start_point = 'Arad'
    end_point = 'Bucharest'
    
    # Executa o algoritmo A* para encontrar o caminho
    path = a_star(graph, start_point, end_point)

    # Limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Imprimir informações iniciais
    print("-| Algoritmo A* |-")
    print("\nOrigem:", start_point)
    print("Destino:", end_point)
    
    # Verifica se foi encontrado um caminho
    if path:
        print("\nCaminho encontrado:", path, "\n")
    else:
        print("\nNão foi possível encontrar um caminho.\n")
