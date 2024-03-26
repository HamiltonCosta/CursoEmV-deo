'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg e o menor foi de {}Kg. '.format(maior, menor))
