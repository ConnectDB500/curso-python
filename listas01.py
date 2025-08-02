# As listas sao mutaveis

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

print(lanche[3])

print(lanche.append('biscoito'))

print(lanche.insert(0, 'coxinha'))

del lanche[3]
print(lanche)

lanche.insert(3, 'pudim')

print(lanche.pop(3))

print(lanche.remove('pizza'))

print(lanche.pop())

if 'pizza' in lanche:
  lanche.remove('pizza')
print(lanche)

galera = []
dado = []
totMai = totMen = 0
for c in range(0, 3):
  dado.append(str(input('nome: ')))
  dado.append(int(input('idade: ')))
  galera.append(dado[:])
  dado.clear()

for p in galera: 
  if p[1] >= 21:
    print(f'{p[0]} e maior de idade')
    totMai += 1
  else: 
    print(f'{p[0]} e menor de idade')
    totMen += 1

print(f'Temos {totMai} maiores e {totMen} menores de idade')