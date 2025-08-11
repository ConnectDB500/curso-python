from geopy.geocoders import nominatim
geolocator = nominatim(user_agent = "wazeyes")

latitude = float(input("digite a latitude ...: "))
longitude = float(input("digite a longitude ...: "))

resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(",")
if resultado[0] != "nome":
  print("endereco completo ...:", resultado)
  print("bairro ..............:", resultado[0])
  print("cidade ..............:", resultado[1])
  print("regiao ..............:", resultado[2])