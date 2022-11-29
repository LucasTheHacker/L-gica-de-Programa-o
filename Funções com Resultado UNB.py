#Distancia entre dois pontos
import math
def quadrado(a1,a2):
    quadrado = (a1 - a2)**2
    return quadrado
def distancia(x1,y1,x2,y2):
    return math.sqrt(quadrado(x1,x2) + quadrado(y1,y2))
#Inverte ordem 
def trocaOrdem(set1,set2):
    return(set2","set1)
#Termo geral da P.A
def n_termo(i, r, n):
    An = i + (n-1)*r
    return An
#Maior entre 3
def max2(a,b):
    if a>b:
        return a
    elif a == b:
        return None
    else:
        return b
def max3(a,b,c):
    maiorab = max2(a,b)
    if maiorab > c:
        return maiorab
    elif maiorab == c:
        return None
    else:
        return c
        
