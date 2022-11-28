#1019 BEECROWD/URI
entrada = int(input())
horas = entrada//3600
restoH = entrada%3600
minutos = restoH//60
segundos = restoH%60
print(f'{horas}:{minutos}:{segundos}')

#1020 BEECROWD/URI
dias = int(input())
ano = dias//365
mes = (dias%365)//30
dias = (dias%365)%30
print(f'{ano} ano(s)\n{mes} mes(es)\n{dias} dia(s)')

#1021
valorfloat = float(input())
inteiro = int(valorfloat)
valor = valorfloat//1
moedas = valorfloat%1
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

print('NOTAS:')
print(f'{nota100:.0f} nota(s) de R$ 100.00')
print(f'{nota50:.0f} nota(s) de R$ 50.00')
print(f'{nota20:.0f} nota(s) de R$ 20.00')
print(f'{nota10:.0f} nota(s) de R$ 10.00')
print(f'{nota5:.0f} nota(s) de R$ 5.00')
print(f'{nota2:.0f} nota(s) de R$ 2.00')

moedas = valorfloat - inteiro
m1 = resto6
moedasint = moedas*100 #Se não converter para inteiro ele trabalha com arredondamento em 2 casas decimais, dando WRONG ANSWER
m50 = moedasint//50
resto1 = moedasint%50 
m25 = resto1//25
resto2 = resto1%25
m10 = resto2//10
resto3 = resto2%10
m05 = resto3//5
resto4 = resto3%5
m01 = resto4//1

print('MOEDAS:')
print(f'{m1:.0f} moeda(s) de R$ 1.00')
print(f'{m50:.0f} moeda(s) de R$ 0.50')
print(f'{m25:.0f} moeda(s) de R$ 0.25')
print(f'{m10:.0f} moeda(s) de R$ 0.10')
print(f'{m05:.0f} moeda(s) de R$ 0.05')
print(f'{m01:.0f} moeda(s) de R$ 0.01')
