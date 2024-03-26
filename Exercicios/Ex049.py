'''
Refaça o DESAFIO 009,
mostrando a tabuada de um número
que o usuário escolher, só que agora
utilizando um laço for.
'''
def tabuada(numero, limite):
    for i in range(1, limite + 1):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
numero = int(input('Digite um número para a tabuada: '))
limite = int(input('Digite até que número deseja multiplicar: '))

tabuada(numero, limite)

