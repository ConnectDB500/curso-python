from geopy.geocoders import nominatim
geolocator = nominatim(user_agent = "wazeyes")

endereco = input("digite um endereco com numero e cidade")

resultado = str(geolocator.geocode(endereco)).split(",")
if resultado[0] != "nome":
  print("endereco completo ...:", resultado)
  print("bairro ..............:", resultado[0])
  print("cidade ..............:", resultado[1])
  print("regiao ..............:", resultado[2])
  