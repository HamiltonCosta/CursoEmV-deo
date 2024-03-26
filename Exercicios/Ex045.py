"""Crie um programa que faça o computador jogar Jokenpô (Pedra, Papel ou Tesoura) com você."""
import random

while True:
    print('''\n\033[1;33mEscolha uma opção: \033[m
\033[0;34m[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura\033[m''')


    escolha_jogador = input('\033[1;33mDigite o número da sua escolha:\033[m')

    if escolha_jogador in ['1', '2', '3']:
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        escolha_computador = random.choice(opcoes)

        if escolha_jogador == '1':
            escolha_jogador = 'Pedra'
        elif escolha_jogador == '2':
            escolha_jogador = 'Papel'
        elif escolha_jogador == '3':
            escolha_jogador = 'Tesoura'

        print("Você escolheu:", escolha_jogador)
        print("O computador escolheu:", escolha_computador)

        if escolha_jogador == escolha_computador:
            print("Empate!")
        elif (escolha_jogador == 'Pedra' and escolha_computador == 'Tesoura') or \
                (escolha_jogador == 'Papel' and escolha_computador == 'Pedra') or \
                (escolha_jogador == 'Tesoura' and escolha_computador == 'Papel'):
            print("Você ganhou!")
        else:
            print("Você perdeu!")
    elif escolha_jogador == '4':
        print("Saindo do jogo...")
        break
    else:
        print("Escolha inválida. Por favor, escolha uma opção válida.")