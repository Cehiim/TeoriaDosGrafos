from TGrafoND import GrafoND

# Grafo como uma matriz de adjacência não-direcionado rotulado
class GrafoNDR(GrafoND): # Ex 8
    def insereA(self, v, w, p):
        if(v == w):
            return
        if self.adj[v][w] == 0:
            self.adj[v][w] = p
            self.adj[w][v] = p
            self.m += 1  # atualiza qtd arestas

    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]:.2f} ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )


	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida 
    # Apresentando apenas os valores 0 ou 1	
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                print(f" {self.adj[i][w]:.2f} ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )