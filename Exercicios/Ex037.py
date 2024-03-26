"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal """
numero = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal ''')
opção = int(input(('Sua opção: ')))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido em Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} convertido em Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opão invadida, tente novamente ...')

