'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
op = 0
while op != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior número
    [4]Novos números
    [5]Sair do programa''')
    op = int(input('Qual é a sua opção? '))

    if op == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')

    elif op == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é de {produto}.')

    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')

    elif op == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))

    elif op == 5:
        print('Finalizando ....')
        sleep(0.6)
    else:
        print('Opção inválida. Tente novamente. ')
    print('=-=' * 30)
print('\033[33mFim do programa.')
