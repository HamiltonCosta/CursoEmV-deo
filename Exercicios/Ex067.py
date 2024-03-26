'''
Faça um programa que mostre a tabuada de vários números,
um de acda vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    num = int(input('Digite um número para ver sua tabuada: (Número negativo encerra o programa)  '))
    if num < 0:
        break
    cont = int(input('Informe até qual número quer a tabuada: '))
    for i in range(1, cont+1):
        print(f'{num} x {i} = {num*i}')
print('Tabuada encerrada!')
