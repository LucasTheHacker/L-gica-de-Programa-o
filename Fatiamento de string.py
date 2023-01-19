lista = input().split()
inicio, fim = input().split()
inicio = int(inicio)
fim = int(fim)
for i in range(len(lista)):  #torna os elementos da lista inteiros
    lista[i] = int(lista[i])
def fatiamento(iniciorandom, fimrandom):
    print(lista[iniciorandom:fimrandom]) #não usar return, praxedes bugado

fatiamento(inicio, fim) 