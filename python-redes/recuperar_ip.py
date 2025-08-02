import socket

resp = "s"
while(resp == "s"):
  url = input("digite uma url: ")
  ip = socket.gethostbyname(url)
  print("O IP referente a url informada: ", ip)
  resp = input("Digite <s> para continuar: ").upper()