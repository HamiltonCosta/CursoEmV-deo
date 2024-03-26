'''
Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até ele acertar,
mostrando no final quantos palpites foram necessários para vencer.

#game antigo

from random import randint
print('=' * 20)
print('== Vou pensar em um número entre 0 e 5. Tente adivinhar.... ==')
print('=' * 20)
num = int(input('Em que número eu pensei ?'))
computador = randint(0,5) #Faz o computador "pensar"
if computador == (num):
    print('Você me venceu!')
    print('Eu pensei no número {}'.format(computador))
else:
    print('Você perdeu!')
    print('Eu pensei no número {}'.format(computador))
'''
from random import randint
computador = randint(0 , 10) #Faz o computador "pensar"
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue acertar ?''')
acertou = False
while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print('Mais... Tente novamente. ')
        elif palpite > computador:
            print('Menos... Tente novamente. ')
print('Acertou!')
