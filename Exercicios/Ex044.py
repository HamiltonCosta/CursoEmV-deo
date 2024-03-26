"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condiçao de pagamento:
-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal(sem juros)
-3x ou mais no cartão: 20% de juros"""

print('\033[1;36m{:=^40}\033[m'.format(' LOJAS HAMILTON '))
valor = float(input('\033[1;33mPreço das compras:\033[m '))
print('''\033[0;34mEscolha a forma de pagamento: 
[ 1 ] À vista em dinheiro ou cheque: 10% de desconto.
[ 2 ] À vista no cartão: 5% de desconto. 
[ 3 ] Em até 2x no cartão: preço normal (Sem Juros).
[ 4 ] 3x ou mais no cartão: 20% de juros. \033[m''')
opção = int(input('\033[0;32mQual vai ser sua forma de pagamento? \033[m'))
if opção == 1:
    pf = valor - (valor * 10 / 100)
    print('\033[0;33mPagando à vista em dinheiro ou cheque você ganha um desconto de 10$ e a sua compra de R${} passa a custa R${}\033[m'.format(valor, pf))
elif opção == 2:
    pf = valor - (valor * 5 / 100)
    print('\033[0;33mPagando à vista no cartão a sua compra de R${} tem um desconto de 5% e passa a custar R${}\033[m'.format(valor, pf))
elif opção == 3:
    pf = valor
    print('\033[0;33mO preço parmance o mesmo pagando em 2x sem juros no cartão. R${}\033[m'.format(pf))
elif opção == 4:
    pf = valor + (valor * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    totaparc = pf / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(parcelas, pf))

'''print('\033[0;33mEm 3x ou mais no cartão tem um acréscimo de 20% de juros fazendo o preço sair de R${} para R${}\033[m'.format(valor, pf))'''

