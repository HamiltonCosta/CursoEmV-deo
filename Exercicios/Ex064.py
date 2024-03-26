'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag(999)).
'''
num = cont = soma = 0
num = float(input('Digite um número. [Digite 999 para finalizar]: '))
while num != 999:
    cont += 1
    soma += num
    num = float(input('Digite um número. [Digite 999 para finalizar]: '))
print(f'Você digitou {cont} e a soma entre eles é de {soma}')
print('\033[32mFim')
