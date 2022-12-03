import math
#B maior que C e D maior que A e c + D maior que A+B e C >0 e D > 0
#A for par
#1035 - Teste de Seleção - BEECROWD/URI
A, B, C , D = map(int, input().split())
def condicoes():
    Bec = B > C
    DeA = D > A
    BD = Bec and DeA #Bec and DeA
    cdab = (C + D) > (A + B)
    Cpos = C > 0
    cC = cdab and Cpos #cdab and Cpos
    Dpos = D > 0
    Apar = A%2 == 0
    Dap = Dpos and Apar #Dpos and Apar
    Tudo = BD and cC and Dap
    if Tudo:
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')
condicoes()

#1036 - Continuar
import math
a, b , c = map(float, input().split())
if a != 0:
    delta = b**2 - 4*a*c
    if delta >= 0:
        raizdelta = math.sqrt(delta)
        R1 = (-b + raizdelta)/(2*a)
        R2 = (-b - raizdelta)/(2*a)
        print(f'R1 = {R1:.5f}')
        print(f'R2 = {R2:.5f}')
    else:
        print('Impossivel calcular')
else:
    print('Impossivel calcular') 
