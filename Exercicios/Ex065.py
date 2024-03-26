'''
Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valor lido. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.
'''
resp = 'S'
soma = count = media = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    media = soma / count
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar ? [S/N] ')).strip() .upper()
print(f'Você digitou {count} números e a média foi de {media} !')
print(f'O maior número é {maior} e o menor é {menor}!')


