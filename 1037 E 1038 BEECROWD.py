#1037 Intervalo - Seleção
entrada = float(input())
if entrada >= 0 and entrada <= 25:
    print(f'Intervalo [0,25]')
elif entrada > 25 and entrada <= 50:
    print(f'Intervalo (25,50]')
elif entrada > 50 and entrada <= 75:
    print(f'Intervalo (50,75]')
elif entrada > 75 and entrada <= 100:
    print(f'Intervalo (75,100]')
else:
    print(f'Fora de intervalo')
#1038 Código - Seleção
codigox, qtdx = map(int, input().split())
if codigox == 1:
    codigox = 4.0
elif codigox == 2:
    codigox = 4.5
elif codigox == 3:
    codigox = 5.0
elif codigox == 4:
    codigox = 2.0
elif codigox == 5:
    codigox = 1.5
def calcule():
    global codigox
    global qtdx
    calculo = codigox * qtdx
    print(f'Total: R$ {calculo}')
calcule()
