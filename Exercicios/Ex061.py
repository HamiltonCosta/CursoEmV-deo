'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
'''
first = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = first + (10 - 1) * razao
for c in range(first, decimo + razao, razao):
    print('{}'.format(c), end='> ')
print('Acabou')
'''
print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += razao
    cont += 1
print('FIM')
