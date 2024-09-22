from TGrafo import Grafo
import os, time

grafo = Grafo() #Cria objeto grafo
while(True):
    choice = int(input(
'''
Menu:
    1) Ler dados do arquivo em python
    2) Gravar dados no arquivo grafo.txt
    3) Inserir vértice
    4) Inserir aresta
    5) Remove vértice
    6) Remove aresta
    7) Mostrar conteúdo do arquivo
    8) Mostrar grafo
    9) Apresentar a conexidade do grafo e o reduzido
    10) Encerrar a aplicação
'''))
    if choice == 1: # Lê grafo
        grafo.leGrafo("palavras.txt")
        print("Grafo lido com sucesso!")
    
    elif choice == 2: # Grava dados no arquivo .txt
        print("oi")

    elif choice == 3: # Insere vértice
        print("oi")
    
    elif choice == 4: # Insere aresta
        print("oi")

    elif choice == 5: # Remove vértice
        print("oi")

    elif choice == 6: # Remove varesta
        print("oi")

    elif choice == 7: # Imprime arquivo
        print("oi")

    elif choice == 8: # Exibe grafo
        print("oi")

    elif choice == 9: # Apresenta a conexidade do grafo e grafo reduzido
        print("oi")

    elif choice == 10: # Encerra
        exit()
    
    else:
        print("Escolha inválida!")
    
    time.sleep(4) # Volta para o menu após 4 segundos
    os.system('clear') # Limpa o terminal