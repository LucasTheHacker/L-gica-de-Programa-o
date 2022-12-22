#Recebe string
#printa elementos nos índices ímpares, exceto espaços
string = input()
indice = 0
tamanho_str = len(string)
while indice < len(string): #indexação começa no zero
    if string[indice] != " " and (indice % 2) != 0: 
        print(string[indice], end="")
    indice += 1