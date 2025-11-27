'''Funções Lambda
a = lambda x: x * 2
print(a(4))

List comprehensions
l = [x for x in range(10)]
print(l)
z = [s.upper() for s in 'abcde']
print(z)
p = [x for x in range(10) if x % 2 == 0]
print(p)

Match case'''
cor = 'Azul'
match cor:
    case 'Vermelho':
        print('A cor é vermelho.')
    case 'Azul':
        print('A cor é azul.')
    case 'Verde':
        print('A cor é verde.')
    case _:
        print('Cor desconhecida.')
