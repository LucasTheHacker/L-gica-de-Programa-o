contador = 0 #Variável auxiliar do loop
lista = [] #lista auxiliar do loop
valor = int(input())
while contador <= valor:
    if contador % 3 == 0 and contador % 7 == 0:
        lista.append(contador)
    contador += 1
for item in lista:
    print(item, end=" ")