#Esse programa analisa se os 3 valores de entrada formam, ou não, um triângulo
#lei de formação: |a-b| < c < a+b
import math 
a, b, c = map(float, input().split())

def verifica():
    global a
    global b
    global c
    bc = b-c
    ac = a-c
    ba = b-a
    condicao_a = (a > math.fabs(bc)) and (a < (b+c)) #A função math.fabs calcula o valor absoluto
    condicao_b = (b > math.fabs(ac)) and (b < (a+c)) #É necessário utilizá-lo pois o resultado da subtração pode ser negativo
    condicao_c = (c > math.fabs(ba)) and (c < (b+a)) #É possível fazer manualmente, com uma função de condicionais...
    if condicao_a and condicao_b and condicao_c:
        perimetro = (a+b+c)
        print(f'Perimetro = {perimetro:.1f}')
    else: #Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura
        areatrapezio = (a+b)*c/2
        print(f'Area = {areatrapezio:.1f}') 
verifica()
    
