'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''
phrase = str(input('Digite uma frase: ')).strip().upper()
palavras = phrase.split()
junto = ''.join(palavras)
inverso = ''
'''
sem utilizar o ' for '

inverso = junto[::-1]
'''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}'.format(phrase, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
