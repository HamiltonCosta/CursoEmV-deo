'''
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 16,
            'Compasso', 15.2)
print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<33}', end='')
    else:
        print(f'R${listagem[item]:>5.2f}')
print('-' * 40)
