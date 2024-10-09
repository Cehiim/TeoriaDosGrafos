# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""
from structure import *
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

    def percursoProfindidade(self, vInicio):
        percurso = [vInicio]
        nosMarcados = []
        pilha = Stack()
        
        nosMarcados.append(vInicio)
        pilha.push(vInicio)
        while(not pilha.isEmpty()):
            
            n = pilha.pop()
            while (self.noAdjacente(n, nosMarcados)) != -1: 
                m = self.noAdjacente(n, nosMarcados)
                percurso.append(m)
                pilha.push(n)
                nosMarcados.append(m)
                n = m

        return percurso

    def percursoLargura(self, vInicio):
        percurso = [vInicio]
        nosMarcados = []
        fila = Queue()

        nosMarcados.append(vInicio)
        fila.enqueue(vInicio)
        while(not fila.isEmpty()):

            n = fila.dequeue()
            while(self.noAdjacente(n, nosMarcados) != -1):
                m = self.noAdjacente(n, nosMarcados)
                percurso.append(m)
                fila.enqueue(m)
                nosMarcados.append(m)

        return percurso
    
    def ordenacaotopologica(self):
        ge = [0] * self.n
        fila = Queue()
        ordenacao = []
        for i in range(self.n):
            ge[i] = self.inDegree(i)
        
        for i in range(self.n):
            if ge[i] == 0:
                fila.enqueue(i)
                ge[i] = -1
        
        while not fila.isEmpty():
            n = fila.dequeue()
            ordenacao.append(n) #visita nó
            for i in range(self.n):
                if self.EhAdjacente(n, i):
                    ge[i] -= 1
            
            for i in range(self.n):
                if ge[i] == 0:
                    fila.enqueue(i)
                    ge[i] = -1

        return ordenacao
    
    def substitui(self, vetor):
        for i in range(self.n):
            vetor[i] = chr(vetor[i] + 97) # Troca os índices da tabela pelas letras dos vértices
        return vetor

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
    
    def _atinge(self, conta_vertice, arvore_parcial, arestas, origem):
        if origem in conta_vertice:
            return True
        
        conta_vertice.append(origem)
        proximas_arestas = [aresta for aresta in arestas if origem in (aresta[0], aresta[1])]
        if len(proximas_arestas) == 0:
            return False
        
        for aresta in proximas_arestas:
            if aresta[0] == origem:
                prox = aresta[1]
            else:
                prox = aresta[0]
            result = self._atinge(conta_vertice, arvore_parcial, arestas, prox)
            if result == True:
                return True
    
        return False
        
    def kruskal(self):
        arestas = []
        for i in range(self.n):
            for j in range(i, self.n):
                if self.adj[i][j] > 0:
                    aresta = (i, j, self.adj[i][j])
                    arestas.append(aresta)
        arestas.sort(key=lambda x: x[-1])
        
        arvore_parcial = []
        for i in range(self.n):
            vertice1 = arestas[i][0]
            vertice2 = arestas[i][1]
            print(arvore_parcial)
            result1 = self._atinge([vertice2], arvore_parcial, arestas, vertice1)
            result2 = self._atinge([vertice1], arvore_parcial, arestas, vertice2)

            if not(result1 or result2):
                arvore_parcial.append(aresta[i])
                
        
        for i in range(len(arvore_parcial)):
            arvore_parcial[i][0] += 1 #Corrige número dos vértices para exibição
            arvore_parcial[i][1] += 1
            
        return arvore_parcial

