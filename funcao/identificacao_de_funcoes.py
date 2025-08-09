def PreencherInventario(lista):
  resp = "s"
  while resp == "s":
    equipamento = [
      input("equipamento: "),
      float(input("valor: ")),
      int(input("numero serial: ")),
      input("departamento: ")
    ]
    lista.append(equipamento)
    resp = input("digite \'s\' para continuar").upper()

def ExibirInventario(lista):
  for elemento in lista:
    print("nome ..............:", elemento[0])
    print("valor .............:", elemento[1])
    print("serial ............:", elemento[2])
    print("departamento ......:", elemento[3])

def LocalizarPorNome(lista):
  busca = input("\n Digite o nome do equipamento que deseja buscar: ")
  for elemento in lista:
    if busca == elemento[0]:
      print("valor .....:", elemento[1])
      print("serial ....:", elemento[2])

def DepreciarPorNome(lista, porc):
  depreciacao = input("\n Digite o nome do equipamento que sera depreciado: ")
  for elemento in lista:
    if depreciacao == elemento[0]:
      print("valor antigo: ", elemento[1])
      elemento[1] = elemento[1] * (1 - porc/100)
      print("novo valor: ", elemento[1])

def ExcluirPorSerial(lista):
  serial = int(input("\n Digite o serial do equipamento que sera excluido: "))
  for elemento in lista:
    if elemento[2] == serial:
      lista.remove(elemento)
    return "Item excluido"

def ResumirValores(lista):
  valores = []
  for elemento in lista:
    valores.append(elemento[1])
  if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("o total de equipamentos e de: ", sum(valores))