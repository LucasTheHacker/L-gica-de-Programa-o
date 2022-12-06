#1044 Beecrowd
a, b = map(int, input().split())
if a%b == 0 or b%a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
#1045 Beecrowd
lista = map(float, input().split())
lista = sorted(lista, reverse=True)
#criando uma lista
a = lista[0]
b = lista[1]
c = lista[2]
if a >= b + c:
    print(f'NAO FORMA TRIANGULO')
if a**2 == b**2 + c**2:
    print(f'TRIANGULO RETANGULO')
if a**2 > b**2 + c**2:
    print(f'TRIANGULO OBTUSANGULO')
if a**2 < b**2 + c**2:
    print(f'TRIANGULO ACUTANGULO')
if a == b and a==c:
    print(f'TRIANGULO EQUILATERO')
elif a == b or a == c or b == c:
    print(f'TRIANGULO ISOSCELES')
