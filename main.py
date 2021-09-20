
numeros = [10,20,5,30,1,3]
print(numeros)

for i in range(5):
  if numeros[i]>numeros[i+1]:
    aux = numeros[i]
    numeros[i]= numeros[i+1]
    numeros[i+1]= aux

print (numeros)

