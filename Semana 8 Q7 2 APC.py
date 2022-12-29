#Questão sobre palíndromos
string = input()
string_reversa = list(reversed(string))
contador = 0
checador = 0
checador_reverso = 0
tamanho = len(string)
#Caso seja do tipo glxlg
for letra in string:
    if letra == string_reversa[contador]:
        checador += 1
    if letra != string_reversa[contador]:
        checador_reverso += 1
    contador +=1
if checador == tamanho and tamanho%2 != 0: #string de tamanho ímpar
    print('ON')
elif checador == tamanho and not(tamanho%2 != 0): #string de tamanho par
    print('OFF')
elif checador_reverso == 2:
    print('ON')
elif checador_reverso > 2:
    print('OFF')
