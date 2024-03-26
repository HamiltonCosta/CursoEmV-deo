'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA(Progressão aritmética. No final, mostre os 10 primeiros termos dessa progressão.'''
first = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = first + (10 - 1) * razao
for c in range(first, decimo + razao, razao):
    print('{}'.format(c), end='> ')
print('Acabou')
