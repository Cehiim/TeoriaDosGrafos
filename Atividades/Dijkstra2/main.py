from TGrafo import Grafo

grafo = Grafo("./Dijkstra2/grafo_anterior.txt") # Grafo da atividade anterior
print("Caminhos mínimos do grafo da atividade anterior:", grafo.dijkstra(3))

grafo2 = Grafo("./Dijkstra2/grafo_aula.txt") # Grafo de exemplo utilizado nas aulas
print("Caminhos mínimos do grafo utilizado como exemplo na aula:", grafo2.dijkstra(1))