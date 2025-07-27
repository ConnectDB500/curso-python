# Tuplas não suportam receber valores atribuidos, pos são imutáveis

lanche = ("hamburger", "suco", "pizza", "pudim")

print(lanche[2])

print(lanche[0:2])

print(lanche[1:])

print(len(lanche))

for c in lanche:
  print(c)

print(lanche[0])

print(lanche[-2])

print(lanche[1:3])

print(lanche[2:])

print(lanche[:2])

print(lanche[-3:])

for comida in lanche:
  print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[cont]} na posicao{cont}')

for pos, comida in enumerate(lanche):
  print(f'Eu vou comer esse {comida} na mesa {pos}')
print("Estou satisfeito!")