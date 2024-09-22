from TGrafo import Grafo
from TGrafoND import GrafoND
from TGrafoR import GrafoR
from TGrafoNDR import GrafoNDR
from TGrafoL import GrafoL

def ehCompleto(grafo): # Ex 26 - Funciona para todos os grafos
    n = grafo.n
    for i in range(n):
        for j in range(n):
            if(i == j):
                if(grafo.adj[i][i] != 0):
                    return False
            else:
                if(grafo.adj[i][j] != 1):
                    return False
    return True

def removeVertice(grafo, vertice): # Ex 9
    n = grafo.n
    if(vertice >= n):
        return False
    for i in range(n-1):
        if(i >= vertice): # Substitui as conexões do vértice a ser retirado e
                          # os vértices posteriores a ele com as conexões do próximo vértice
            grafo.adj[i] = grafo.adj[i+1]
        if(grafo.adj[i][vertice] == 1): # Remove as arestas conectadas no vértice escolhido
            grafo.adj[i][vertice] = 0
            grafo.m -= 1 # Subtrai o número de arestas
        grafo.adj[i].pop(vertice) # Remove o vértice escolhido da linha da matriz
    grafo.adj.pop() # Remove a última linha da matriz
    grafo.n -= 1 # Subtrai o número de vértices
    return True

def grafoComplementar(grafo): # Ex 12
    n = grafo.n
    grafo_complementar = Grafo(n)
    for i in range(n):
        for j in range(n):
            if(grafo.adj[i][j] == 0):
                grafo_complementar.insereA(i, j)
    return grafo_complementar

def matrizParaLista(matriz): # Ex 18
    n = matriz.n
    lista = GrafoL(n)
    for i in range(n):
        for j in range(n):
            if(matriz.adj[i][j] == 1):
                lista.insereA(i, j)
    return lista

def comparaGrafos(matriz, lista): # Ex 17
    if(matriz.n != lista.n or matriz.m != lista.m):
        return "Os grafos são diferentes"
    n = matriz.n
    for i in range(n):
        for j in range(n):
            if(matriz.adj[i][j] == 0):
                if(j in lista.listaAdj[i]):
                    return "Os grafos são diferentes"
            else:
                if(not j in lista.listaAdj[i]):
                    return "Os grafos são diferentes"
    return "Os grafos são iguais"
'''
print("Grafo original")
g = GrafoND(6)
g.insereA(0, 1)
g.insereA(1, 2)
g.insereA(2, 0)
g.insereA(2, 3)
g.insereA(3, 4)
g.insereA(3, 5)
g.insereA(4, 5)
g.insereA(5, 3)
#g.show()
g.showMin()
print(g.ehCompleto())
#print(g.conexidade())
#removeVertice(g,4)
g.removeV(4)
g.showMin()

print("Grafo complementar")
gc = grafoComplementar(g)
gc.showMin()

print("Grafo em lista")
gl = matrizParaLista(g)
gl.show()
print(comparaGrafos(g,gl))

gnd = GrafoNDR(4)
gnd.insereA(0, 1)
gnd.insereA(0, 2)
gnd.insereA(0, 3)
gnd.insereA(1, 2)
gnd.insereA(1, 3)
gnd.insereA(2, 3)
gnd.insereA(3, 3)
#gnd.show()
gnd.showMin()
print(g.ehCompleto())
'''
gr = GrafoNDR(4)
gr.insereA(0, 1, 1.5)
gr.insereA(0, 2, 3)
gr.insereA(0, 3, 4.5)
gr.insereA(1, 2, 1)
gr.insereA(1, 3, 3.5)
gr.insereA(2, 3, 2)
gr.insereA(3, 3, 5)
#gr.show()
gr.showMin()
