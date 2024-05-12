# Tuplas são imutáveis
'''
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('=' * 40)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('=' * 40)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('=' * 40)

print('Comi pra caramba!')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
#print(c.index(8))
#print(c.count(5))
#print(len(c))
#print(sorted(c))
'''
pessoa = ('Gustavo', 39, 'M', 99.24)
print(pessoa)
