def contador(i,f, p):
  """
  -> 'contador()' faz uma contagem e mostra
    para i: inicio
    para f: fim
    para p: passo
  """
  c = 1
  while c <= f:
    print(f"{c}", end=" ")
    c += p
  print("Fim!")

help(contador)
print(contador.__doc__)