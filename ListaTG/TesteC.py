from TGrafo import Grafo
from TGrafoND import GrafoND

def ehCompleto(grafo): # Ex 11
    n = grafo.n
    for i in range(n):
        for j in range(n):
            if(i == j):
                if(grafo.adj[i][i] == 1):
                    return False
            else:
                if(grafo.adj[i][j] != 1):
                    return False
    return True
                
g = Grafo(4)
#insere as arestas do grafo

g.insereA(0, 1)
g.insereA(0, 2)
g.insereA(0, 3)
g.insereA(1, 2)
g.insereA(1, 3)
g.insereA(2, 1)
g.insereA(2, 3)
g.insereA(3, 3)
# mostra o grafo preenchido
#g.show()
g.showMin()
print(ehCompleto(g))
