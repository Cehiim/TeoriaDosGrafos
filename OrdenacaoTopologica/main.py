from TGrafo import Grafo

grafo = Grafo() #Obtém grafo do arquivo .txt
ordenacao_topologica = grafo.ordenacaotopologica() #Obtém lista com a ordenação topológica do grafo
ordenacao = grafo.substitui(ordenacao_topologica) #Substitui os índices dos vértices por letras

print("Lista com a ordenação topológica:", ordenacao) # Imprime a lista
