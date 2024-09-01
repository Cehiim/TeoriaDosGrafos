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
            return "O grafo é completo"
        else:
            return "O grafo não é completo"
                
    def conexidade(self): # Ex 13
        if(self.n > 1 and self.m == 0):
            return "O grafo não é conexo"
        passou = [0]
        for i in range(self.n):
            if(not i in passou):
                return "O grafo não é conexo"
            for j in range(self.n):
                if(i != j and self.adj[i][j] != 0 and not j in passou):
                    passou.append(j)
                    #print(passou)
        return "O grafo é conexo"