'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
mais alguns termos.O programa encerra quando ele disser que quer
mostrar 0 termos.
'''
print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
tot= 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')