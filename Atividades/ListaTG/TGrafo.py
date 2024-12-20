# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""

# Grafo como uma matriz de adjacência
class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # matriz de adjacência
        self.adj = [[0 for i in range(n)] for j in range(n)]

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
    #OBS: Estou assumindo que, para os métodos abaixo, o valor v pertence ao intervalo [0, n - 1] ao invés de [1, n], em que n é o número de vértices
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
    def leGrafo(self, path = "grafo.txt"):
        with open(path, 'r') as file:
            self.n = int(file.readline())
            self.m = int(file.readline())
            for _ in range(self.m):
                string = file.readline()
                i, j = int(string[0]), int(string[2])
                self.adj[i][j] = 1
    
    #Método para remover um vértice de um grafo direcionado Ex 25)
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
        
    def ehCompleto(self): # Ex 11
        if((self.n ** 2) - self.n == self.m):
            return "O grafo é completo"
        return "O grafo não é completo"

    def dfs(self, visitados, vertice): # Depth First Search
        visitados[vertice] = True
        for i in range(self.n):
            if(self.adj[vertice][i] != 0 and visitados[i] == False): # Caso haja acesso para um próximo vértice que não foi visitado
                self.dfs(visitados, i)

    def ehForte(self):
        count = 0
        for i in range(self.n):
            visitados = [False] * self.n
            self.dfs(visitados, i)
            if(all(visitados)): # Caso todos tenham sido visitados
                count += 1
        if(count == self.n):
            return True
        else:
            return False

    def ehSemiForte(self):
        for i in range(self.n):
            for j in range(self.n):
                visitados = [False] * self.n
                self.dfs(visitados, j)
                if(visitados[i] == False): # Verifica se o vértice 'j' tem acesso para o vértice 'i'
                    visitados = [False] * self.n
                    self.dfs(visitados, i)
                    if(visitados[j] == False): # Verifica se o vértice 'i' tem acesso para o vértice 'j'
                        return False
        return True

    def removeDirecao(self):
        grafo_nd = Grafo(self.n)
        for i in range(self.n):
            for j in range(self.n):
                if(self.adj[i][j] != 0):
                    grafo_nd.insereA(i,j)
                    grafo_nd.insereA(j,i)
        return grafo_nd

    def ehSimples(self):
        grafo_nd = self.removeDirecao() # Versão não-direcionada do grafo original
        for i in range(self.n):
            visitados = [False] * self.n
            grafo_nd.dfs(visitados, i)
            if(all(visitados)): # Caso todos tenham sido visitados
                return True
        return False

    def conexidade(self):
        if(self.ehForte()):
            print("O grafo é fortemente conexo (C3)")
        else:
            if(self.ehSemiForte()):
                print("O grafo é semi-fortemente conexo (C2)")
            else:
                if(self.ehSimples()):
                    print("O grafo é simplesmente conexo (C1)")
                else:
                    print("O grafo é desconexo (C0)")

    def fechoDireto(self, visitados):
        fecho_direto = []
        for i in range(self.n):
            if(visitados[i]):
                fecho_direto.append(i) # Adiciona os vértices acessíveis
        return fecho_direto

    def fechoInverso(self, vertice):
        visitados = [False] * self.n
        fecho_inverso = []
        for i in range(self.n):
            self.dfs(visitados, vertice)
            if(visitados[vertice]):
                fecho_inverso.append(i) # Adiciona os vértices que acessam
        return fecho_inverso
