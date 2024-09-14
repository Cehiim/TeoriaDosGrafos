from TGrafo import Grafo

# Teste 1
grafo = Grafo() #Obtém grafo do arquivo .txt
ordenacao_topologica = grafo.ordenacaotopologica() #Obtém lista com a ordenação topológica do grafo
ordenacao = grafo.substitui(ordenacao_topologica) #Substitui os índices dos vértices por letras

print("Lista com a ordenação topológica:", ordenacao) # Imprime a lista

# Teste 2
grafo2 = Grafo("./OrdenacaoTopologica/outro_grafo.txt") #Obtém grafo do arquivo .txt
topologica2 = grafo2.ordenacaotopologica() #Obtém lista com a ordenação topológica do grafo

print("Lista com a ordenação topológica:", topologica2) # Imprime a lista