#Checa se uma string é, ou não, um palíndromo
string = input()
string_reversa = list(reversed(string))
controle = len(string)
meio = (controle -1)//2
contador = 0
diferencas = 0
while contador < controle: #loop para verificar quantas diferenças existem entre a string original e a string de trás pra frente
    if string[contador] != string_reversa[contador]: #conta as diferenças
        diferencas += 1
    contador += 1
if diferencas == 2:
    print('ON')
elif diferencas == 0 and controle%2 == 0: #caso seja uma palavra de quantidade de letras par
    print('OFF')
elif string[meio] == string_reversa[meio]: #caso especial para as palavras que podem trocar a letra do meio e continuam sendo palíndromos
    print('ON')
else:
    print("OFF")

#fccf