'''2-'''
carros = {
    'nome': ['Celta', 'Up', 'Kombi', 'Uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
    
}

def forca_opcao(msg, opcoes):
    msg += '\n' + '\n'.join(opcoes) + '\n'
    escolha = input(msg)
    while escolha not in opcoes:
        print('Resposta inválida.')
        escolha = input(msg)
    return escolha

def acha_indice(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
        
def informacoes(dic, i):
    for key in dic.keys():
        print(f'{key}: {carros[key][i]}')
    return

'''opcao = forca_opcao('Escolha uma das opções a seguir para ver suas informações:', carros['nome'])
indice = acha_indice(carros['nome'], opcao)
informacoes(carros, indice)

3-'''
def indice_mais_caro(lista):
    i_mais_caro = 0
    for i in range(len(lista)):
        if lista[i] > lista[i_mais_caro]:
            i_mais_caro = i
    return i_mais_caro

'''indice = indice_mais_caro(carros['preço'])
informacoes(carros, indice)

4-'''
def indice_mais_barato(lista):
    i_mais_barato = 0
    for i in range(len(lista)):
        if lista[i] < lista[i_mais_barato]:
            i_mais_barato = i
    return i_mais_barato

'''indice = indice_mais_barato(carros['preço'])
informacoes(carros, indice)

5-'''

def add_elem(dic):
    for key in dic.keys():
        novo_elem = input(f'{key}: ')
        carros[key].append(novo_elem)

'''opcao = forca_opcao('Você gostaria de adicionar um novo carro?', ['Sim', 'Não'])
if opcao == 'Sim':
    add_elem(carros)
    print(carros)
else:
    print('Tudo bem, obrigado!')
    
6-
opcao = forca_opcao('Qual dos carros você gostaria de remover?', carros['nome'])
indice = acha_indice(carros['nome'], opcao)
for key in carros.keys():
    carros[key].pop(indice)
print(carros)

7-'''
frase = 'O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será.'
frase.lower()
for char in '.,':
    frase = frase.replace(char, '')
palavras = frase.split()
contador = {}
for palavra in palavras:
    if palavra not in contador:
        contador[palavra] = 1
    else:
        contador[palavra] += 1
print(contador)









