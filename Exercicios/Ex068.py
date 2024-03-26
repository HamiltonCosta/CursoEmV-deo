'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador Perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
v = 0
while True:
    player = int(input('Digite um valor: '))
    pc = randint(0, 10)
    total = player + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {player} e o computador {pc}. Total de {total}')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente ...')

print(f'GAME OVER! Você venceu {v} vezes.')



