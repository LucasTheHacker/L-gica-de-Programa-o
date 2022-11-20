#|Plataforma: Beecrowd|Problema 1012|Linguagem: Python|Nível: iniciante|
A,B,C = map(float, input().split())

areatriangulo = (A*C/2)

areacirculo = (3.14159 * C**2)

areatrapezio = ((A+B)*C/2)

areaquadrado = B**2

arearetangulo = A*B

print(f'TRIANGULO: {areatriangulo:.3f}')

print(f'CIRCULO: {areacirculo:.3f}')

print(f'TRAPEZIO: {areatrapezio:.3f}')

print(f'QUADRADO: {areaquadrado:.3f}')

print(f'RETANGULO: {arearetangulo:.3f}')
