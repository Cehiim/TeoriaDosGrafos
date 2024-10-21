# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""

import sys

# Grafo como uma matriz de adjacência
class GrafoND:
    # construtor da classe grafo
    def __init__(self, path):
        self.leGrafo(path)

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.m+=1 # atualiza qtd arestas
    
# remove uma aresta v->w do Grafo
    def removeA(self, v, w):
        if(v == w):
            return
        # testa se temos a aresta
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m -= 1  # atualiza qtd arestas

	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(f"Adj[{i:2d},{w:2d}] = 1 ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )


	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida 
    # Apresentando apenas os valores 0 ou 1	
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(" 1 ", end="") 
                else:
                    print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )


    # Função para calcular o grau de entrada no vértice v Ex 1)
    #OBS: Estou assumindo que, para os métodos abaixo, o valor v pertence ao intervalo [0, n - 1] ao invés de [1, n]
    def inDegree(self, v):
        degree = 0
        for i in range(self.n):
            degree += self.adj[i][v]
        return degree
    
    #Função para calcular o grau de saída no vértice v Ex 2)
    def outDegree(self, v):
        degree = 0
        for i in range(self.n):
            degree += self.adj[v][i]
        return degree
    
    #Função para verificar se um vértice é fonte Ex 3)
    def ehFonte(self, v):
        if(self.inDegree(v) == 0 and self.outDegree(v) > 0):
            return 1
        else:
            return 0
    
    #Função para verificar se um vértice é sorvedouro Ex 4)
    def ehSoverdouro(self, v):
        if(self.inDegree(v) > 0 and self.outDegree(v) == 0):
            return 1
        else:
            return 0

    #Função para verificar se um grafo é simétrico Ex 5)    
    def ehSimetrico(self):
        for i in range(self.n):
            for j in range(i, self.n):
                if(self.adj[i][j] != self.adj[j][i]):
                    return 0
        return 1
    
    #Método para ler um grafo de um arquivo .txt Ex 6)
    def leGrafo(self, path):
        with open(path, 'r') as file:
            self.n = int(file.readline())
            self.m = int(file.readline())

            # matriz de adjacência
            self.adj = [[0 for i in range(self.n)] for j in range(self.n)]
            for _ in range(self.m):
                string = file.readline()
                i, j, k = string.split(" ")
                i, j, k = int(i), int(j), int(k)
                i -= 1
                j -= 1
                self.adj[i][j] = k
                self.adj[j][i] = k
    
    #Método para remover um vértice de um grafo Ex 9)
    def removeV(self, v):
        for i in range(self.n):
            if self.adj[i][v] == 1 or self.adj[v][i] == 1: #Verifica se havia uma aresta para subtrair
                self.m -= 1
            if i != v and i != len(self.adj) - 1: #Substitui a linha e coluna da matriz a serem apagadas pelas últimas linha e coluna respectivamente
                self.adj[i][v] = self.adj[i][-1]
                self.adj[v][i] = self.adj[-1][i]

        self.adj[v][v] = self.adj[-1][-1]
        for i in range(self.n):
            self.adj[i].pop() #Remove a última coluna da matriz
        
        self.adj.pop() #Remove a última linha
        self.n -= 1 #Decrementa um vértice
    
    def noAdjacente(self, n, nosMarcados):
        for i, item in zip(range(len(self.adj[n])), self.adj[n]):
            if item == 1 and i not in nosMarcados:
                return i
        return -1
    
    def EhAdjacente(self, v, x): #verifica se o vértice v é adjacente a x
        if self.adj[v][x] == 1:
            return True
        else:
            return False
    
    def substitui(self, vetor):
        vetor_copia = vetor.copy()
        for i in range(self.n):
            vetor_copia[i] = chr(vetor_copia[i] + 97) # Troca os índices da tabela pelas letras dos vértices
        return vetor_copia

    def dijkstra(self, origem):
        # Inicializar distâncias com "infinito"
        origem -= 1
        distancias = [sys.maxsize] * self.n
        distancias[origem] = 0  # A distância da origem para ela mesma é 0

        # Conjunto de vértices visitados
        visitados = set()

        # Enquanto todos os vértices não forem visitados
        while len(visitados) < self.n:
            # Encontre o vértice com a menor distância que ainda não foi visitado
            min_distancia = sys.maxsize
            u = -1 # menor distância
            for i in range(self.n):
                if i not in visitados and distancias[i] < min_distancia:
                    min_distancia = distancias[i]
                    u = i

            # Marque o vértice `u` como visitado
            visitados.add(u)

            # Atualizar as distâncias dos vizinhos de `u`
            for v in range(self.n):
                if self.adj[u][v] > 0 and v not in visitados:  # Existe uma aresta entre `u` e `v`
                    nova_distancia = distancias[u] + self.adj[u][v]
                    if nova_distancia < distancias[v]:
                        distancias[v] = nova_distancia
                        
        return distancias
    
    def _find(self, parent, i):
        if parent[i] == i:
            return i
        return self._find(parent, parent[i])

    # Função para unir dois subconjuntos no Union-Find
    def _union(self, parent, rank, x, y):
        root_x = self._find(parent, x)
        root_y = self._find(parent, y)

        # Anexar a árvore de menor rank sob a árvore de maior rank
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Implementação do Algoritmo de Kruskal
    def kruskal(self):
        arestas = [] #Obtém as arestas do grafo
        for i in range(self.n):
            for j in range(i, self.n):
                if self.adj[i][j] > 0:
                    aresta = (i, j, self.adj[i][j])
                    arestas.append(aresta)

        # Ordenar as arestas por peso
        arestas.sort(key=lambda x: x[2])

        # Inicializar a estrutura Union-Find
        parent = []
        rank = []

        for node in range(self.n):
            parent.append(node)
            rank.append(0)

        # Lista para armazenar a árvore geradora mínima (MST)
        arvore_parcial = []

        # Número de arestas na MST
        e = 0
        i = 0

        # Iterar pelas arestas em ordem de peso
        while e < self.n - 1 and i < len(arestas):
            # Escolher a menor aresta
            u, v, peso = arestas[i]
            i += 1

            # Encontrar os representantes (subconjuntos) dos vértices u e v
            x = self._find(parent, u)
            y = self._find(parent, v)

            # Se u e v não pertencem ao mesmo subconjunto, adicionar a aresta à MST
            if x != y:
                e += 1
                arvore_parcial.append([u, v, peso])
                self._union(parent, rank, x, y)
        
        for i in range(len(arvore_parcial)): #Ajusta índice dos vértices
            arvore_parcial[i][0] += 1
            arvore_parcial[i][1] += 1

        # Exibe a árvore geradora mínima
        self._show_kruskal(arvore_parcial)

    def _show_kruskal(self, arvore_parcial):
        print("Arestas da árvore Parcial de Custo mínimo:")
        print("Vertice1 --- Vertice2 --- Peso")
        for i in range(len(arvore_parcial)):
            print(f"{arvore_parcial[i][0]} --- {arvore_parcial[i][1]} --- {arvore_parcial[i][2]}")

    def colore_sequencial(self):
        lista_colorida = self.n * [0]
        for i in range(self.n):
            other_colors = []
            for j in range(self.n):
                if self.EhAdjacente(i, j) and lista_colorida[j] != 0:
                    other_colors.append(lista_colorida[j])
            
            if other_colors == []:
                lista_colorida[i] = 1

            elif other_colors != []:
                for k in range(1, self.n):
                    if k not in other_colors:
                        lista_colorida[i] = k
                        break
                    
        return lista_colorida
