#Implemente um algoritmo que leia um número inteiro, em seguida calcule o fatorial deste número e apresente para o usuários.
#Ex: n = 4
#O Fatorial de 4 é 24

n= 5
for i in range (2,n):
  n = n*i
print(n)




fatorial= 1
n= 4
for i in range (n):
  fatorial= fatorial*n
  n= n-1

print(fatorial)