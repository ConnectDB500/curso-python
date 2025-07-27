import getpass # Permite pegar a senha do usuário sem exibi-la na tela
import telnetlib

HOST = "router_ip"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn= telnetlib.Telnet(HOST) # Abre uma conexão Telnet com o roteador.

tn.read_until(b"login: ") # Aguarda o prompt de login
tn.write(user.encode("ascii") + b"\n") # Envia o nome de usuário.

# Se uma senha foi digitada, aguarda o prompt Password: e envia a senha.
if password: 
  tn.read_until(b"Password: ")
  tn.write(password.encode("ascii") + b"\n")

# Cria duas interfaces de loopback (0 e 1) com IPs 1.1.1.1 e 2.2.2.2.
tn.write(b"conf t\n")  # Entra no modo de configuração global
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"int loop 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")

tn.write(b"router ospf 1\n") #Inicia o processo OSPF nº 1.
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n") # Adiciona todas as interfaces com wildcard mask 0.0.0.0 255.255.255.255

tn.write(b"end\n") # Sai do modo de configuração.
tn.write(b"exit\n")

print(tn.read_all().decode("ascii")) # Lê e exibe toda a saída do terminal Telnet até o final da sessão.