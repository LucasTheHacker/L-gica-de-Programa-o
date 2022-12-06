#1044 Beecrowd
a, b = map(int, input().split())
if a%b == 0 or b%a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
    
#1045 Beecrowd
lista = map(float, input().split())
#A lista, quando os inputs são dados na mesma linha, é criada de forma automática...
lista = sorted(lista, reverse=True) #Colocando a lista ordenada de forma decrescente
a = lista[0]
b = lista[1]
c = lista[2]
if a >= b + c:
    print(f'NAO FORMA TRIANGULO')
elif a**2 == b**2 + c**2:
    print(f'TRIANGULO RETANGULO')
elif a**2 > b**2 + c**2:
    print(f'TRIANGULO OBTUSANGULO')
if a**2 < (b**2 + c**2):
    print(f'TRIANGULO ACUTANGULO')
if a == b and a==c:
    print(f'TRIANGULO EQUILATERO')
elif a == b or b ==c:
    print(f'TRIANGULO ISOSCELES')
#Utilização de listas
