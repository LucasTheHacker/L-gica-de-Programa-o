a, b , c = map(float, input().split())
tipo = input()
if tipo == 'P':
    pa, pb, pc = map(float, input().split())
else:
    pass
#A utilização dessas condicionais se dá pelo EOF quando tipo != P.
#A terceira linha de input só se dará nos casos de média ponderada.
if tipo == 'A':
    media_aritmetica = (a + b + c)/3
if tipo == 'H':
    media_harmonica = 3/ (1/a + 1/b +1/c)
if tipo == 'P':
    media_ponderada = ((a*pa)+(b*pb)+(c*pc))/(pa+pb+pc)


def calculo():
    if tipo == 'P':
        print('Ponderada')
        print(f'{media_ponderada:.2f}')
    elif tipo == 'H':
        print('Harmonica')
        print(f'{media_harmonica:.2f}')
    elif tipo == 'A':
        print('Aritmetica')
        print(f'{media_aritmetica:.2f}')
    else:
        print('Operacao inexistente')

calculo()