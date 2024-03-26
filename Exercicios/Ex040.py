"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO"""
n1 = float(input('\033[0;35mPrimeira nota : \033[m'))
n2 = float(input('\033[0;35mSegunda nota : \033[m'))
media = (n1 + n2) / 2
print('\033[0;34mTirando {:.1f} e {:.1f}, a média do aluno é {:.1f}\033[m'.format(n1, n2, media))
if media < 5:
    print('\033[1;31mVocê foi REPROVADO!\033[m')
elif 7 > media >= 5:
    print('\033[0;33mVocê está de RECUPERAÇÃO\033[m')
elif media >= 7:
    print('\033[1;32mVocê foi APROVADO\033[m')
