'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
par = 0
for num in range(1, 7):
    num = int(input('{}ª - Digite um número: '.format(num)))
    if num % 2 == 0:
        par = num + par
print('A soma dos números PARES é: {}'.format(par))

