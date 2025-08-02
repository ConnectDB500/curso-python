import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account")
password = getpass.getpass()

f = open("myswitches.txt")

for IP in f:
  IP = IP.strip()
  print("Configurando o Switchy: " + (IP))
  HOST = IP
  tn = telnetlib.Telnet(HOST)
  tn.read_until(b"Username: ")
  tn.write(user.encode('ascii') + b"\n")
  if password:
    tn.read_untiol(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")

for i in range(50,71):
  tn.write(b"vlan " + str(i).encode('ascii') + "\n")
  tn.write(b"name PYTHON_VLAN_" + str(i).encode('ascii') + "\n")

tn.write(b"end\n")
tn.write(b"exit\n")
