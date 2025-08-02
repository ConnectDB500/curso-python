teste = list()

teste.append('Gustavo')
print(teste)

teste.append(40)

galera = list()

galera.append(teste)
print(galera)

print(teste[0])

print(teste[1])

#
pessoas = [['Joao', 19], ['Ana', 33], ['Joaquim', 13]]
for p in pessoas:
  print(f'{p[0]} tem {p[1]} anos de idade')