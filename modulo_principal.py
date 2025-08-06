minhaLista = []

print("preenchendo ...")
PreencherInvetario(minhaLista)

print("exibindo ...")
ExibirInventario(minhaLista)

print("pesquisando ...")
LocalizarPorNome(minhaLista)

print("excluindo ...")
DepreciarPorNome(minhaLista, 20)

print("excluido ...")
print(ExcluiPorSerial(minhaLista))
ExibirInventario(minhaLista)

print("resumindo ...")
ResumirValores(minhaLista)