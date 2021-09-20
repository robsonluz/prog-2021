
numeros = [8,3,9,4,3,4,1,3,2]
print(numeros)
for j in range(len(numeros) - 1):
  for i in range(len(numeros) - 1):
    if numeros[i]  > numeros[i + 1]:
      aux = numeros[i]
      numeros[i]= numeros[i + 1]
      numeros[i + 1]= aux

print (numeros)

