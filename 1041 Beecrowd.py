#Recebe duas coordenadas e informa o quadrante ou eixo que o ponto se encontra.
import math
x, y = map(float, input().split())
if x > 0 and y > 0:
    print('Q1')
elif x > 0 and y < 0:
    print('Q4')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x == 0 and y != 0:
    print('Eixo Y')
elif y == 0 and x != 0:
    print('Eixo X')
else:
    print('Origem')
    
    