from TGrafo import Grafo
from TGrafoND import GrafoND
from TGrafoNDR import GrafoNDR
from TGrafoR import GrafoR

# Fazer 1 ao 6 e 9 e 10
'''
grafo = Grafo(6)

grafo.leGrafo()
for i in range(grafo.n):
    print(grafo.adj[i])
print()
grafo.removeV(2)
for i in range(grafo.n):
    print(grafo.adj[i])
'''

grafoND = GrafoND(6)
grafoND.leGrafo()
for i in range(grafoND.n):
    print(grafoND.adj[i])

print(grafoND.ehCompleto())

