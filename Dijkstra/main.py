from TGrafo import Grafo


grafo = Grafo()
print(grafo.dijkstra(3))

#Teste grafo da aula
grafo2 = Grafo("./Dijkstra/grafo_teste.txt") #Obtém grafo do arquivo .txt
print(grafo2.dijkstra(1))