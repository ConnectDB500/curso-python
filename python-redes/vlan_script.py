for x in range (2, 9):
  print('vlan ', str(x))

import getpass
import telnetlib

HOST = "switch_ip"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")

if password:
  tn.read_until(b"Password: ")
  tn.write(password.encode("ascii") + b"\n")

# Entra no modo de configuração e cria VLANs:
tn.write(b"conf t\n")

for x in range (2, 10):
  tn.write(b"vlan " + str(x).encode('ascii') + b"\n")
  tn.write(b"name PYTHON_VLAN_" + str(x).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode("ascii"))