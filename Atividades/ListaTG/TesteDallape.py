from TGrafo import Grafo
from TGrafoND import GrafoND
from TGrafoNDR import GrafoNDR
from TGrafoR import GrafoR

class GrafoSimples:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas
        self.matriz_adj = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
        for (u, v) in arestas:
            self.matriz_adj[u][v] = 1

    def number_of_nodes(self):
        return len(self.vertices)

    def number_of_edges(self):
        return len(self.arestas)

    def tem_ciclo(self):
        visitados = [False] * len(self.vertices)
        rec_stack = [False] * len(self.vertices)

        def ciclo_dfs(v):
            visitados[v] = True
            rec_stack[v] = True

            for i in range(len(self.vertices)):
                if self.matriz_adj[v][i] == 1:
                    if not visitados[i]:
                        if ciclo_dfs(i):
                            return True
                    elif rec_stack[i]:
                        return True

            rec_stack[v] = False
            return False

        for nodo in range(len(self.vertices)):
            if not visitados[nodo]:
                if ciclo_dfs(nodo):
                    return True
        return False

    def dfs_edges(self):
        visitados = [False] * len(self.vertices)
        edges = []

        def dfs(v):
            visitados[v] = True
            for i in range(len(self.vertices)):
                if self.matriz_adj[v][i] == 1 and not visitados[i]:
                    edges.append((v, i))
                    dfs(i)

        for nodo in range(len(self.vertices)):
            if not visitados[nodo]:
                dfs(nodo)

        return edges

    def dfs_util(self, v, visitados, stack):
        visitados[v] = True
        for i in range(len(self.vertices)):
            if self.matriz_adj[v][i] == 1 and not visitados[i]:
                self.dfs_util(i, visitados, stack)
        stack.append(v)

    def transpose(self):
        g_transposto = GrafoSimples(self.vertices, [])
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self.matriz_adj[i][j] == 1:
                    g_transposto.matriz_adj[j][i] = 1
        return g_transposto

    def dfs_explorar(self, v, visitados, componente):
        visitados[v] = True
        componente.append(v)
        for i in range(len(self.vertices)):
            if self.matriz_adj[v][i] == 1 and not visitados[i]:
                self.dfs_explorar(i, visitados, componente)

    def cfc(self):
        stack = []
        visitados = [False] * len(self.vertices)

        # Passo 1: Preencher a pilha com base na ordem de finalização do DFS
        for i in range(len(self.vertices)):
            if not visitados[i]:
                self.dfs_util(i, visitados, stack)

        # Passo 2: Criar o grafo transposto
        g_transposto = self.transpose()

        # Passo 3: Fazer DFS no grafo transposto de acordo com a pilha
        visitados = [False] * len(self.vertices)
        componentes = []

        while stack:
            v = stack.pop()
            if not visitados[v]:
                componente = []
                g_transposto.dfs_explorar(v, visitados, componente)
                componentes.append(componente)

        return componentes

class GrafoListaAdjacencia:
    def __init__(self, vertices, arestas, dirigido=False):
        self.vertices = vertices
        self.lista_adj = {v: [] for v in vertices}
        self.dirigido = dirigido
        for u, v in arestas:
            self.lista_adj[u].append(v)
            if not dirigido:
                self.lista_adj[v].append(u)  # Adiciona a aresta inversa para grafos não dirigidos

    def imprime_lista_adj(self):
        for vertice in self.lista_adj:
            print(f"{vertice}: {self.lista_adj[vertice]}")

    def inverte_grafo(self):
        grafo_invertido = {v: [] for v in self.vertices}

        for u in self.lista_adj:
            for v in self.lista_adj[u]:
                grafo_invertido[v].append(u)

        self.lista_adj = grafo_invertido

    def eh_fonte(self, vertice):
        grau_saida = len(self.lista_adj[vertice])
        grau_entrada = 0

        for v in self.lista_adj:
            if vertice in self.lista_adj[v]:
                grau_entrada += 1

        if grau_saida > 0 and grau_entrada == 0:
            return 1  # É uma fonte
        else:
            return 0  # Não é uma fonte

    def eh_sorvedouro(self, vertice):
        grau_saida = len(self.lista_adj[vertice])
        grau_entrada = 0

        for v in self.lista_adj:
            if vertice in self.lista_adj[v]:
                grau_entrada += 1

        if grau_saida == 0 and grau_entrada > 0:
            return 1  # É um sorvedouro
        else:
            return 0  # Não é um sorvedouro

    def eh_simetrico(self):
        for u in self.lista_adj:
            for v in self.lista_adj[u]:
                # Verifica se há uma aresta de v para u
                if u not in self.lista_adj[v]:
                    return 0  # Não é simétrico
        return 1  # É simétrico

    def from_file(nome_arquivo):
        with open(nome_arquivo, 'r') as file:
            linhas = file.readlines()

            # A primeira linha contém o número de vértices
            V = int(linhas[0].strip())

            # A segunda linha contém o número de arestas (não é necessário usar diretamente)
            A = int(linhas[1].strip())

            # As demais linhas contêm as arestas
            arestas = []
            for linha in linhas[2:]:
                u, v = map(int, linha.strip().split())
                arestas.append((u, v))

            # Cria uma lista de vértices de 0 a V-1
            vertices = list(range(V))

            # Retorna uma instância de GrafoListaAdjacencia
            return GrafoListaAdjacencia(vertices, arestas)

    def remover_vertice(self, vertice):
        if vertice not in self.lista_adj:
            print(f"Vértice {vertice} não encontrado no grafo.")
            return

        # Remove o vértice da lista de adjacência de todos os outros vértices
        for v in self.lista_adj:
            if vertice in self.lista_adj[v]:
                self.lista_adj[v].remove(vertice)

        # Remove o vértice e suas arestas
        del self.lista_adj[vertice]
        self.vertices.remove(vertice)

    def eh_completo(self):
        V = len(self.vertices)
        for u in self.vertices:
            for v in self.vertices:
                if u != v:
                    if self.dirigido:
                        # Para grafos dirigidos, verifica a presença de arestas de u para v e v para u
                        if v not in self.lista_adj[u] or u not in self.lista_adj[v]:
                            return 0  # Não é completo
                    else:
                        # Para grafos não dirigidos, verifica a presença de aresta entre u e v
                        if v not in self.lista_adj[u]:
                            return 0  # Não é completo
        return 1  # É completo

def classificar_complexidade(grafo):
    if grafo.number_of_nodes() == 0:
        return 'C0'  # Grafo vazio

    if grafo.number_of_edges() == 0:
        return 'C1'  # Grafo com um único vértice ou sem arestas

    if grafo.tem_ciclo():
        return 'C3'  # Grafo tem ciclos

    if len(grafo.dfs_edges()) > 0:
        return 'C2'  # Grafo não tem ciclos, mas tem caminhos com mais de um vértice

    return 'C1'  # Grafo sem ciclos, todos os caminhos com exatamente um vértice

def grafo_reduzido(grafo):
    componentes = grafo.cfc()
    mapeamento = {}
    for i, componente in enumerate(componentes):
        for v in componente:
            mapeamento[v] = i

    matriz_reduzida = [[0 for _ in range(len(componentes))] for _ in range(len(componentes))]

    for u, v in grafo.arestas:
        if mapeamento[u] != mapeamento[v]:
            matriz_reduzida[mapeamento[u]][mapeamento[v]] = 1

    return matriz_reduzida

def inverte_grafo(grafo):
    grafo_invertido = {v: [] for v in grafo.vertices}

    for u in grafo.lista_adj:
        for v in grafo.lista_adj[u]:
            grafo_invertido[v].append(u)

    grafo.lista_adj = grafo_invertido


# Exemplo de uso:
vertices = [0, 1, 2, 3]
arestas = [(0, 1), (1, 2), (2, 3), (0, 3)]
grafo = GrafoSimples(vertices, arestas)
print(classificar_complexidade(grafo))  #Ex 14
print('\n')
matriz_reduzida = grafo_reduzido(grafo) #Ex 15
print(matriz_reduzida)

grafoadj = GrafoListaAdjacencia(vertices, arestas)

print("\nGrafo original:")
grafoadj.imprime_lista_adj()

inverte_grafo(grafoadj)

print("\nGrafo invertido:")
grafoadj.imprime_lista_adj() #Ex 19

print("\nGrafo:")
grafoadj.imprime_lista_adj()

# Verificar se o vértice 0 é uma fonte
resultado = grafoadj.eh_fonte(2)
print(f"O vértice 4 é uma fonte? {resultado}")  #Ex 20

# Verificar se o vértice 3 é uma fonte
resultado = grafoadj.eh_fonte(3)
print(f"O vértice 3 é uma fonte? {resultado}")

print("\nGrafo:")
grafoadj.imprime_lista_adj()

# Verificar se o vértice 3 é um sorvedouro
resultado = grafoadj.eh_sorvedouro(3) 
print(f"O vértice 3 é um sorvedouro? {resultado}") #Ex 21

# Verificar se o vértice 0 é um sorvedouro
resultado = grafoadj.eh_sorvedouro(0)
print(f"O vértice 0 é um sorvedouro? {resultado}")

vertices = [0, 1, 2, 3]
arestas_simetricas = [(0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (3, 2)]
arestas_nao_simetricas = [(0, 1), (1, 0), (1, 2), (2, 3)]

grafo_simetrico = GrafoListaAdjacencia(vertices, arestas_simetricas) 
grafo_nao_simetrico = GrafoListaAdjacencia(vertices, arestas_nao_simetricas) #Ex 22

print("\nGrafo simétrico:")
grafo_simetrico.imprime_lista_adj()
resultado = grafo_simetrico.eh_simetrico()
print(f"O grafo é simétrico? {resultado}")

print("\nGrafo não simétrico:")
grafo_nao_simetrico.imprime_lista_adj()
resultado = grafo_nao_simetrico.eh_simetrico()
print(f"O grafo é simétrico? {resultado}") #Ex 23

# Exemplo de uso:
grafo = GrafoListaAdjacencia.from_file('grafo.txt')

print("\nLista de Adjacência do Grafo do arquivo:")
grafo.imprime_lista_adj()

# Remover um vértice
grafo.remover_vertice(2) #Ex 24

print("\nGrafo após remover o vértice 2:")
grafo.imprime_lista_adj()

# Grafo Dirigido
vertices_dirigido = [0, 1, 2]
arestas_dirigido = [(0, 1), (1, 2), (2, 0)]
grafo_dirigido = GrafoListaAdjacencia(vertices_dirigido, arestas_dirigido, dirigido=True)

print("\nGrafo Dirigido:")
grafo_dirigido.imprime_lista_adj()
resultado_dirigido = grafo_dirigido.eh_completo()
print(f"O grafo dirigido é completo? {resultado_dirigido}") #Ex 25

# Grafo Não Dirigido
vertices_nao_dirigido = [0, 1, 2]
arestas_nao_dirigido = [(0, 1), (1, 2), (2, 0)]
grafo_nao_dirigido = GrafoListaAdjacencia(vertices_nao_dirigido, arestas_nao_dirigido, dirigido=False)

print("\nGrafo Não Dirigido:")
grafo_nao_dirigido.imprime_lista_adj()
resultado_nao_dirigido = grafo_nao_dirigido.eh_completo() #Ex 26
print(f"O grafo não dirigido é completo? {resultado_nao_dirigido}")
