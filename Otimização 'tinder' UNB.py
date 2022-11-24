'''D ≤ 100   : ''É o amor da minha vida!"
100 < D ≤ 200 : "Talvez dê certo"
D > 200 : "Não vale a pena investir'''
#A entrada consiste em 4 linhas,sendo as duas primeiras (x1,y1) a localização do usuário e as duas últimas (x2,y2) a localização de sua mais nova paquera.


import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x = ((x1 - x2)**2) + ((y1 - y2)**2)

distancia = math.sqrt(x)

if distancia <= 100:
    print('É o amor da minha vida!')
elif distancia > 100 and distancia <= 200:
    print('Talvez dê certo')
else:
    print("Não vale a pena investir")
    
