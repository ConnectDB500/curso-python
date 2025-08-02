valores = [range(4, 11)]

print(valores)

print(valores.sort())

print(valores.sort(reverse = True))

print(len(valores))

#
num = [2, 5, 9, 11]

num[2] = 3
print(num)

num.append(7)
print(num)

num.insert(2, 0)
print(num)

num.pop(2)
print(num)

num.insert(2, 2)
print(num)

num.remove(2)
print(num)

#
dados  = list()

dados.append('Pedro')
print(dados)

dados.append(25)
print(dados)

print(dados[0])

print(dados[1])

pessoas = list()

pessoas.append(dados[:])

print(pessoas[0][0])

print(pessoas[1][1])
