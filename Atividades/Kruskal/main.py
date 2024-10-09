from TGrafoND import GrafoND

grafo = GrafoND("grafo_anterior.txt") # Grafo da atividade anterior
print("Aplicando o algoritmo de Kruskal no grafo da atividade anterior:", grafo.kruskal())

grafo2 = GrafoND("grafo_aula.txt") # Grafo de exemplo utilizado nas aulas
print("Aplicando o algoritmo de Kruskal no grafo utilizado como exemplo na aula:", grafo2.kruskal())