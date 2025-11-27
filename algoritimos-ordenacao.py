def indice_menor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice

def selection_sort(lista):
    ordenada = []
    qtd = len(lista)
    for i in range(qtd): #ou while lista:
        local_menor = indice_menor(lista)
        menor = lista.pop(local_menor)
        ordenada.append(menor)
    return ordenada

def selection_sort_menos_pior(lista):
    for i in range(len(lista)):
        localmenor = indice_menor(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[localmenor]
        lista[localmenor] = aux
        print(lista)
    return

def bubble_sort(lista):
    for i in range(len(lista)):
        trocas = 0
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                trocas += 1
        if trocas == 0:
            break
    return

def raiz_binaria(num):
    ini = 0
    fim = num
    while fim - ini > 0.001:
        chute = (ini + fim) / 2
        if chute**2 > num:
            fim = chute
        else:
            ini = chute
        print(chute)
    return chute

raiz_binaria(144)