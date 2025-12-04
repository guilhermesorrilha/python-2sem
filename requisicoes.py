import requests

'''requisicao = requests.get('https://requisicoes-beed3-default-rtdb.firebaseio.com/.json')
print(requisicao.json())

informacoes = '{"Nome": "Alexandre Pantoja"}'
requisicao = requests.post('https://requisicoes-beed3-default-rtdb.firebaseio.com/.json', data=informacoes)
print(requisicao.json())'''

informacoes = '{"Idade": "29", "Nome": "Jean Silva"}'
requisicao = requests.patch('https://requisicoes-beed3-default-rtdb.firebaseio.com/2.json', data=informacoes)
print(requisicao.json())

requisicao = requests.delete('https://requisicoes-beed3-default-rtdb.firebaseio.com/-OffTZNzYN9an031LXUp.json')
print(requisicao.json())