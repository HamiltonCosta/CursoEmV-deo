"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do Peso.
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: O:obesidade
-Acima de 40: Obesidade mórbida"""

peso = float(input('Qual é seu peso (kg)? '))
altura = float(input('Qual sua altura (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está em sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida.')

