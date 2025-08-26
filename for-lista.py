'''i = 1
while i < 11:
    print(f'Tabuada do {i}')
    j = 1
    while j < 11:
        print(f'{i} x {j} = {i*j}')
        i+=1
        print()

for i in range(1,11):
    print(f'Tabuada do {i}')
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')

lista = [4, 1, 5, 7, 3, 6, 9, 2, 10, 8]
soma = 0
for num in lista:
    soma += num
media = soma / len(lista)
print(f'A soma dos números da lista é igual a {soma} e a média é {media}')

lista = []
pares = 0
for num in range(1, 11):
    num_usuario = int(input(f'Digite o {num} número: '))
    lista.append(num_usuario)
    if num_usuario % 2 == 0:
        pares += 1
impares = len(lista) - pares
print(f'A lista {lista} possui {pares} números pares e {impares} números impares.')'''