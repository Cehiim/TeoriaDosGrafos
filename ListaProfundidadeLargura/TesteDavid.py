from TGrafo import Grafo

grafo = Grafo(8) #Obtém grafo do arquivo .txt
grafo.leGrafo("./ListaProfundidadeLargura/grafo_teste.txt")
profundidade = grafo.percursoProfindidade(0) #Obtém percurso em largura e profundidade
largura = grafo.percursoLargura(0)

for i in range(grafo.n):
    profundidade[i] = chr(profundidade[i] + 97) # Troca os índices da tabela pelas letras dos vértices
    largura[i] = chr(largura[i] + 97)

print("Percurso em profundidade:", profundidade) # Imprime os percursos
print("Percurso em largura:", largura)
