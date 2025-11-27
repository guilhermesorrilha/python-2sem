import pandas as pd
import requests

acougue = {
    'Carne': ['Picanha', 'Maminha', 'Linguiça', 'Patinho'],
    'Preço/kg': [79.90, 49.90, 14.90, 34.90],
    'Estoque': [10, 12, 18, 14],
    'Validade': [8, 6, 9, 10]
}

def forca_opcao(msg, lista):
    msg += '\n' + '\n'.join(lista) + '\n'
    escolha = input(msg)
    while escolha not in lista:
        print('Opção inválida.')
        escolha = input(msg)
    return escolha

def cria_indices():
    global indices
    indices = {}
    for i in range(len(acougue['Carne'])):
        indices[acougue['Carne'][i]] = i
    return indices

'''def cadastrar():
    global indices
    for key in acougue.keys:
        info = input(f'{key}: ')
        acougue[key].append(info)
    print(pd.DataFrame(acougue))
    indices = cria_indices()
    return'''

def cadastrar():
    global indices
    for key in acougue.keys():
        if 'preço/kg' in key.lower() or 'estoque' in key.lower():
            while True:
                try:
                    info = float(input(f'{key}: '))
                except:
                    print('Por favor digite um número.')
                else: #É executado se a info for um float
                    acougue[key].append(info)
                    break #Sai do while True
            continue #Pula para a próxima chave
        info = input(f'{key}: ')
        acougue[key].append(info)
    print(acougue)
    indices = cria_indices()
    return


def remover():
    item = forca_opcao('Qual das carnes você gostaria de remover?', acougue['Carne'])
    for key in acougue.keys:
        acougue['key'].pop(indices[item])
    print(pd.DataFrame(acougue))
    indices = cria_indices()
    return

def atualizar():
    item = forca_opcao('Qual das carnes você gostaria de atualizar?', acougue['Carne'])
    indice_item = indices[item]
    keys = list(acougue.keys)
    keys.pop(0)
    for key in keys:
        if forca_opcao(f'Você gostaria de atualizar {key} para {item}?', ['Sim', 'Não']) == 'Sim':
            acougue[key][indice_item] = input(f'Digite o novo(a) {key}: ')
    print(pd.DataFrame(acougue))
    return

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        print('A opção escolhida deve ser um número')
        num = input(msg)
    return int(num)

def comprar():
    carne = forca_opcao('De qual carne você gostaria?', acougue['Carne'])
    indice_carne = indices[carne]
    for key in acougue.keys:
        print(f'{key}: {acougue[key][indice_carne]}')
    confirmacao = forca_opcao('Você gostaria de levar a carne?', ['Sim', 'Não'])
    if confirmacao == 'Não':
        return
    qtd = verifica_numero('De quantos kg você gostaria?')
    while qtd > acougue['Estoque'][indice_carne]:
        print('Infelizmente isso é mais do que temos no estoque.')
        qtd = verifica_numero('De quantos kg você gostaria?')
    acougue['Estoque'][indice_carne] -= qtd
    if carne not in carrinho['Itens'].keys():
        carrinho['Itens'][carne] = qtd
    else:
        carrinho['Itens'][carne] += qtd

def cadastro_endereco():
    while True:
        cep = input('Digite o seu CEP: ')
        endereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if endereco.status_code == 200:
            carrinho['Endereço'] = endereco.json()
            carrinho['Endereço']['Número'] = input("Numero da residencia: ")
            carrinho['Endereço']['Complemento'] = input("Complemento: ")
            break
        else:
            print('CEP Inválido.')
    return

carrinho = {
    'Endereço': {},
    'Itens': {},
    'Valor total': 0
}

acoes = {
    'Cadastrar': cadastrar,
    'Remover': remover,
    'Atualizar': atualizar,
    'Sair': exit
}
        



