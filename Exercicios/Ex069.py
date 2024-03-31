'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''
count = tot18 = homens = mulheres = 0
#pergunta a idade e o sexo do usuario.
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade > 20:
        mulheres += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'Total de pessoa com mais de 18 anos cadastradas: {tot18}')
print(f'Total de homens cadastrado: {homens}')
print(f'Total de mulheres com mais de 18 anos: {mulheres}')
