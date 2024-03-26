'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.
'''
somaIdade = 0
mediaIdade = 0
maiorIdade = 0
nomemaisvelho = ''
totmulher20 = 0
quant = int(input('\033[32mQuantas pessoas serão analizadas? ' ))
for c in range(1, quant + 1):
    print(f'----- {c}ªPessoa ------')
    nome = str(input('\033[34mNome: ')).strip()
    idade = int(input('\033[34mIdade: '))
    sexo = str(input('\033[34m[F/M]: ')).upper().strip()
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        maiorIdade = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaIdade = somaIdade / 4
print(f'\033[33mA media de idade do grupo é de {mediaIdade} anos.')
print(f'\033[33mO homem mais velho tem {maiorIdade} anos e se chama\033[m\033[34m {nomemaisvelho}')
print(f'\033[33mAo todo são {totmulher20} mulheres com menos de 20 anos.')
