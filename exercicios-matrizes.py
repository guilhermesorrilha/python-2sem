import matplotlib.pyplot as plt

'''1- 
def printa_matriz(matriz):
    for linha in matriz:
        for elem in linha:
            print(elem, end=' ')
    print()

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

printa_matriz(mat)

2-'''
def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz
    
'''3-
def cria_diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1
    return matriz

mat_teste = cria_matriz(10, 10)
diagonal = cria_diagonal(mat_teste)
plt.imshow(diagonal)
plt.show()

4-
def contra_diagonal_ruim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == len(matriz) - 1 - j:
                matriz[i][j] = 1
    return

def contra_diagonal_bom(matriz):
    for i in range(len(matriz)):
        j = len(matriz) - 1 - i
        matriz[i][j] = 1
    return

mat_teste = cria_matriz(10, 10)
contra_diagonal_bom(mat_teste)
plt.imshow(mat_teste)
plt.show()

5-
def superior_ruim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j > i:
                matriz[i][j] = 1
    return

mat_teste = cria_matriz(10, 10)
superior_ruim(mat_teste)
plt.imshow(mat_teste)
plt.show()

def superior_bom(matriz):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            matriz[i][j] = 1
    return

def superior_inferior(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j != i:
                matriz[i][j] = 1
    return

mat_teste = cria_matriz(10, 10)
superior_inferior(mat_teste)
plt.imshow(mat_teste)
plt.show()'''




