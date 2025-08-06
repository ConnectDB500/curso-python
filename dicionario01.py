dados = dict()
dados = {"nome": "Pedro", "idade": 25}

print(dados["nome"])

print(dados["idade"])

dados["sexo"] = "M"

del dados["idade"]


filme = {
  "titulo": "Star Wars",
  "ano": 1997,
  "diretor": "George Lucas"
  }

print(filme.values())

print(filme.itens())

for k, v in filme.items():
  print(f"O {k} e {v}")

locadora = []
locadora.append({"titulo": "Star Wars", "ano": 1977, "diretor": "George Lucas"})
locadora.append({"titulo": "matrix", "ano": 2012, "diretor": "Joss"})
locadora.append({"titulo": "Matrix", "ano": 1999, "diretor": "Wachowski"})
print(locadora[0]["ano"])
print(locadora[2]["titulo0"])


estado = {}
brasil = []
for c in range(0, 3):
  estado["uf"] = str(input("unidade federativa: "))
  estado["sigla"] = str(input("sigla do estado: "))
  brasil.append(estado.copy())
print(brasil)