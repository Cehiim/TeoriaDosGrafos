from TGrafo import Grafo

# Grafo como uma matriz de adjacência não-direcionado
class GrafoND(Grafo): # Ex 7
    def __init__(self, n):
        super().__init__(n)

    def insereA(self, v, w):
        if(v == w):
            return
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.adj[w][v] = 1
            self.m += 1  # atualiza qtd arestas
    
# remove uma aresta v->w do Grafo
    def removeA(self, v, w):
        if(v == w):
            return
        # testa se temos a aresta
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.adj[w][v] = 0
            self.m -= 1  # atualiza qtd arestas
    
    #Verifica se o grafo é completo Ex 10)
    def ehCompleto(self):
        if((self.n ** 2 - self.n)/ 2 == self.m):
            return True
        else:
            return False