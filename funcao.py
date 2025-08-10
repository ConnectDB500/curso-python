def titulo(tx):
  print("-" * 30)
  print(tx)
  print("-" * 30)

titulo("      CURSO EM VIDEO")
titulo("      APRENDA PYTHON")
titulo("      GUSTAVO GUANABARA")

#
def soma(a, b):
  print(f"A = {a} e B = {b}")
  s = a + b
  print(f"A soma A + B = {s}")

soma(4, 9)

#
def contador(*num):
  size = len(num)
  print(f"Recebi os valores {num} e sao ao todo {size}")

contador(2, 0, 5, 4, 7)

#
def dobra(lista):
  pos = 0
  while pos < len(lista):
    lista[pos] *= 2
    pos += 1

valores = (6, 3, 9, 1, 0, 2)
dobra(valores)

#
def soma(*valor):
  i = 0
  for num in valor:
    i += num
  print(f"somente os valores {valor} temos {i}")