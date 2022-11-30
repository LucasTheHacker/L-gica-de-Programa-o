#Calcula raízes de uma equação do segundo grau
def raizes(a, b, c):
    if a != 0:
        delta = b**2 - 4*a*c       
        if delta > 0:
            return 2
        elif delta == 0:
            return 1
        else:
            return -1

#Problema OBMEP (Adaptado UNB) - Apenas distâncias horizontais ou verticais
import math
def calcula_distancia(x, y, xc, yc):
    deltax = x - xc
    deltay = y - yc
    if deltax >= 0: 
        deltax = deltax
    else:
        deltax = -1*deltax
    if deltay >= 0: 
        deltay = deltay
    else:
        deltay = -1*deltay
    return deltax + deltay
#1, 2, 2, 3, 4, 6, 9, 14, 22, 35, ... -->Função c Resultado
import math
def deivis_sequence(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        sequencia = (deivis_sequence(n-1) + deivis_sequence(n-2) - 1)
        return sequencia
#Maneira alternativa, com função recursiva de se definir um múltiplo de 3
def multiplo3(n):
    if n == 0:
        return True
    elif n == 1 or n == 2:
        return False
    else:
        return multiplo3(n-3)
    
def não_multiplo3(n):
    if n==0:
        return False
    elif n==1 or n==2:
        return True
    else:
        return not multiplo3(n-3)
#Algoritmo de Euclides
import math
def mdc(a,b):
    if a%b == 0:
        return b
    else:
        return mdc(b, (a%b))

    

    
    

    
    
    
