frase = "curso em video python"
print(frase[5])

print(frase[2:7]) # variavel[x:y]  x ate y -1

print(frase[2:7:3]) # variavel[x:y:z] z e a ordem

print(len(frase)) # comprimento da variavel

print(frase.count("o")) 

print(frase.find("video"))

if "python" in frase:
  print("Ta ok")