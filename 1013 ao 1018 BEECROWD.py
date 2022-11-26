#1013 BEECROWD/URI
a, b, c = map(int, input().split())
maior = max(a, b, c)
print(f'{maior} eh o maior')

#1014 BEECROWD/URI
distancia = int(input())
combustivel = float(input())
consumo = distancia/combustivel
print(f'{consumo:.3f} km/l')

#1015 BEECROWD/URI 
import math
X1, Y1 = map(float, input().split())
X2, Y2 = map(float, input().split())
elevado = (X1 - X2)**2 + (Y1 - Y2)**2
distancia = math.sqrt(elevado)
print(f'{distancia:.4f}')

#1016 BEECROWD/URI
distancia = int(input())
calculo = distancia * 2
print(f'{calculo} minutos')

#1017 BEECROWD/URI
'''consumo 12km/l; quantidade de litros = km *l/km'''
tempo = int(input())
velocidade = int(input())
distancia = velocidade * tempo
consumo = 12
litros = distancia/consumo
print(f'{litros:.3f}')

#1018 BEECROWD/URI
valor = int(input())
nota100 = valor//100
resto1 = valor - nota100*100
nota50 = resto1 // 50
resto2 = resto1 - nota50*50
nota20 = resto2 // 20
resto3 = resto2 - nota20*20
nota10 = resto3 // 10
resto4 = resto3 - nota10*10
nota5 = resto4 // 5
resto5 = resto4 - nota5*5
nota2 = resto5//2
resto6 = resto5 - nota2*2
nota1 = resto6 

print(valor)
if valor >= 100:
    print(f'{nota100} nota(s) de R$ 100,00')
else:
    print('0 nota(s) de R$ 100,00')
if resto1 >= 50:
    print(f'{nota50} nota(s) de R$ 50,00')
else:
    print('0 nota(s) de R$ 50,00')
if resto2 >= 20:
    print(f'{nota20} nota(s) de R$ 20,00')
else:
    print('0 nota(s) de R$ 20,00')
if resto3 >= 10:
    print(f'{nota10} nota(s) de R$ 10,00')
else:
    print('0 nota(s) de R$ 10,00')
if resto4 >= 5:
    print(f'{nota5} nota(s) de R$ 5,00')
else:
    print('0 nota(s) de R$ 5,00') 
if resto5 >= 2:
    print(f'{nota2} nota(s) de R$ 2,00')
else:
    print('0 nota(s) de R$ 2,00')    
if resto6 >= 1:
    print(f'{nota1} nota(s) de R$ 1,00')
else:
    print('0 nota(s) de R$ 1,00\n')
#1018 BEECROWD/URI forma alternativa e otimizada
'''Forma otimizada de fazer essa questão, sem a utilização de condicionais'''
valor = int(input())
nota100 = valor//100
resto1 = valor - nota100*100
nota50 = resto1 // 50
resto2 = resto1 - nota50*50
nota20 = resto2 // 20
resto3 = resto2 - nota20*20
nota10 = resto3 // 10
resto4 = resto3 - nota10*10
nota5 = resto4 // 5
resto5 = resto4 - nota5*5
nota2 = resto5//2
resto6 = resto5 - nota2*2
nota1 = resto6
print(valor)
print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00')
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{nota1} nota(s) de R$ 1,00')
