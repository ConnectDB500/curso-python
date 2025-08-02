import socket

domain = socket.getservbyname("domain")
http = socket.getservbyname("http")
ftp = socket.getservbyname("ftp")

print(domain)
print(http)
print(ftp)