'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
'''
total = 0
menor = cont = 0
barato = ''
totmil = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Valor do produto: '))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'O total da compra foi de R${total}')
print(f'Temos {totmil} custando mais de R$1000 ')
print(f'O produto mais barato foi {barato}')
print('Fim do programa')
