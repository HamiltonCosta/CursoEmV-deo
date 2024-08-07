'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (int) e o programa vai informar
quantas cédulas de cada valor serão entregues.
Obs. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
b = "$ Hamilton's Banc $"
print('\033[33m-\033[m\033[32m$\033[m\033[33m-\033[m' * 17)
print(f'\033[32m{b: ^50}\033[m')
print('\033[33m-\033[m\033[32m$\033[m\033[33m-\033[m' * 17)

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('Volte sempre!')

