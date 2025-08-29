import matplotlib.pyplot as plt

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

'''print('Elementos da primeira linha:')
for elem in mat[0]:
    print(elem, end=' ')
print()

print('Todos os elementos de mat:')
for linha in mat:
    for elem in linha:
        print(elem, end=' ')
    print()'''

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = [] #cria uma linha
        for j in range(colunas):
            linha.append(0) #adiciona nessa linha x colunas ou x zeros
        matriz.append(linha) #adiciona essa linha na matriz
    return matriz

def imagem(matriz):
    plt.imshow(matriz, 'hot')
    plt.colorbar()
    plt.show()
    return

def cria_diagonal_ruim(linhas, colunas):
    diagonal = cria_matriz(5, 5)
    for i in range(len(diagonal)):
        for j in range(len(diagonal[0])):
            if i == j:
                diagonal[i][i] = 1
    return diagonal

def cria_diagonal_bom(linhas, colunas):
    diagonal = cria_matriz(linhas, colunas)
    for i in range(len(diagonal)):
        diagonal[i][i] = 1
    return diagonal

xadrez = cria_matriz(8, 8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i % 2 == 0:
            if j % 2 == 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
        else:
            if j % 2 == 0:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0