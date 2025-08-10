try:
  a = int(input("numerador: "))
  b = int(input("denominador: "))
  c = a/b
except Exception as erro:
  print(f"problema encontrado: {erro.__class__.__name__}")
else:
  print(f"resultado: {c:.1f}")
finally:
  print("fim")