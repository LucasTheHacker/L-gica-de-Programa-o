import math
#Esse programa ordena, de maneira crescente, 3 números inteiros
#Depois disso, eles são printados na ordem que entraram
'''Fiz esse código antes de estudar o método sort :'''
a, b, c = map(int, input().split())
def menor(): #utilização de função condicional p definir o menor
    global a
    global b
    global c
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    elif c < b and c < a:
        print(c)
def medio(): #utilização de função condicional p definir o termo médio
    global a
    global b
    global c
    if (a > b and a < c)or(a < b and a > c):
        print(a)
    elif (b > a and b < c)or(b < a and b > c):
        print(b)
    elif (c > a and c < b)or(c < a and c > b):
        print(c)
def maior(): #Utilização de função condicional p/ definir o termo maior
    global a
    global b
    global c
    if a > b and a > c:
        print(a)
    if b > a and b > c:
        print(b)
    if c > b and c > a:
        print(c)
menor()
medio()
maior()
print('')
print(a)
print(b)
print(c)       