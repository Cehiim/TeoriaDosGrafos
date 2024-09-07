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

#grafoND = GrafoND(6)
#grafoND.leGrafo()
#for i in range(grafoND.n):
#    print(grafoND.adj[i])
#
#print(grafoND.ehCompleto())

###### Testa Busca em profundidade ########
grafo = Grafo(8)

profundidade = grafo.percursoProfindidade(0)
largura = grafo.percursoLargura(0)

for i in range(grafo.n):
    profundidade[i] = chr(profundidade[i] + 97)
    largura[i] = chr(largura[i] + 97)

print("Percurso em profundidade:", profundidade)
print("Percurso em largura:", largura)
