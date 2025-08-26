'''def media(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista)
    return media

notas = [9, 8, 10, 6]
media_1 = media(notas)
print(media_1)

def local_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            indice_maior = i
            maior = lista[indice_maior]
    return indice_maior

def forca_opcao(lista, msg):
    opcoes = '\n'.join(lista)
    opcao = input(f'{msg}\n{opcoes}')
    while opcao not in lista:
        print('Resposta inválida.')
        opcao = input(msg)
    return opcao

def acha_indice(elem, lista):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

carros = ['up', 'gol', 'polinho turbão manual', 'uno']

CP 3'''
print('Bem-vindo!')
def forca_num(msg):
    num = input(msg)
    while not num.isnumeric():
        print('Resposta inválida, digite apenas números.')
        num = input(msg)
    return int(num)
ano_nascimento = forca_num('Digite o ano do seu nascimento: ')
idade = 2025 - ano_nascimento
if idade < 18:
    print('Não é permitido a venda de bebidas alcoólicas para menores de 18 anos.')
else:
    endereco = input('Digite o seu endereço: ')
    def media(lista):
        soma = 0
        for num in lista:
            soma += num
        media = soma / len(lista)
        return media
    vinhos = ['George St. Pierre', 'Benoît St. Denis', 'Murrici Ruffy', 'Cyril Gane', 'Sharaputdin']
    precos = [170, 80, 90, 100, 70]
    custo_medio = media(precos)
    def local_maior(lista):
        indice_maior = 0
        maior = lista[indice_maior]
        for i in range(len(lista)):
            if lista[i] > maior:
                indice_maior = i
                maior = lista[indice_maior]
        return indice_maior
    maior_preco = local_maior(precos)
    vinho_mais_caro = vinhos[maior_preco]
    def local_menor(lista):
        indice_menor = 0
        menor = lista[indice_menor]



    
