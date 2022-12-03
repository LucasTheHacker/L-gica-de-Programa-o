#Esse programa analisa as notas de um aluno em 3 situações
import math
n1, n2, n3, n4 = map(float, input().split())
#media ponderada = n1*p1 + n2*p2.../(p1+p2...)
p1 = 2
p2 = 3
p3 = 4
p4 = 1
calculo = ((n1*p1)+(n2*p2)+(n3*p3)+(n4*p4))/(p1+p2+p3+p4)
#utilizei função somente para treinar... Não é estritamente necessária aqui
def ponderada():
    global n1, n2, n3, n4
    global p1, p2, p3, p4
    global calculo
    #calculo calcula a media ponderada
    return calculo
print(f'Media: {ponderada():.1f}')
#É bem melhor fazer a utilização do aninhamento de condicionais aqui.
if ponderada() >= 7:
    print(f'Aluno aprovado.')
elif ponderada() >= 5 and ponderada() <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    #Nesse momento, recalcula-se a média
    medrecalc = (calculo + exame)/2
    if medrecalc >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {medrecalc:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {medrecalc:.1f}')
else:
    print(f'Aluno reprovado.')
        

        
        
