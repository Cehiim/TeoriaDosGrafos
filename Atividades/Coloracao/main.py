from TGrafoND import GrafoND

grafo = GrafoND("grafo_licao.txt") # Grafo da atividade anterior
print("Aplicando o algoritmo de coloração de vértices sequencial no grafo da lição anterior:")
lista_colorida = grafo.colore_sequencial()
numeros = [i for i in range(grafo.n)]
letras = grafo.substitui(numeros)

for elem1, elem2 in zip(letras, lista_colorida): # Relaciona os vértices com suas respectivas cores
    print(f'{elem1:<2} -> {elem2}')


grafo2 = GrafoND("grafo_aula.txt") # Grafo da atividade anterior
print("\nAplicando o algoritmo de coloração de vértices sequencial no grafo da aula:")
lista_colorida2 = grafo2.colore_sequencial()
numeros2 = [i for i in range(1, grafo.n + 1)]

for elem1, elem2 in zip(numeros2, lista_colorida2): # Relaciona os vértices com suas respectivas cores
    print(f'{elem1:<2} -> {elem2}')