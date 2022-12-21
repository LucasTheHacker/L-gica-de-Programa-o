
#Palavra Nova
string = input()
tamanho = len(string) #para achar as duas últimas
duas_primeiras = string[0:2]
duas_ultimas = string[tamanho-2:] #pensamento da questão
print(duas_primeiras+duas_ultimas) 

#Números
string = input()
tamanho_string = len(string)
posicao = 0
controle = 0
while posicao < tamanho_string:
    if string[posicao] == '0' or string[posicao] == '1' or string[posicao] == '2' or string[posicao] == '3' or string[posicao] == '4' or string[posicao] == '5' or string[posicao] == '6' or string[posicao] == '7' or string[posicao] == '8' or string[posicao] == '9':
        controle += 1
    posicao += 1
print(controle)
