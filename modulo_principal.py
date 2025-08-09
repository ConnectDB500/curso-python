from funcao.identificacao_de_funcoes import *

minhaLista = []

print("preenchendo ...")
PreencherInventario(minhaLista)

print("exibindo ...")
ExibirInventario(minhaLista)

print("pesquisando ...")
LocalizarPorNome(minhaLista)

print("excluindo ...")
DepreciarPorNome(minhaLista, 20)

print("excluido ...")
print(ExcluirPorSerial(minhaLista))
ExibirInventario(minhaLista)

print("resumindo ...")
ResumirValores(minhaLista)