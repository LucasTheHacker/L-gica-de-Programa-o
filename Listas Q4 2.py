lista = input().split()
for i in range(len(lista)):  #transforma os elementos da lista em int
    lista[i] = int(lista[i])
for i in range(len(lista)): #autodescritivo
    if i == 0:
        primeiro = lista[i]
    else:
        primeiro = primeiro*2  
        segundo = lista[i]*1/2
        primeiro += segundo
print(f'{primeiro:.2f}')