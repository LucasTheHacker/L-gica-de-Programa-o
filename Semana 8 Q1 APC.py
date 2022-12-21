#Verifica se ha um caractere especifico numa string
#Jeito correto e inteligente de fazer:
posicao = 0
caractere = ','
string = input()
tamanho_string = len(string)
controle = 'variavel somente de controle do caso o while seja'
while posicao < tamanho_string and string[posicao != ","]:
    if caractere == string[posicao]:
        print("passed")
        controle = 1
    posicao += 1
if controle != 1:
    print('failed')
#Jeito pythõnico e malandro de se fazer
#Verifica se ha um caractere especifico numa string
posicao = 0
caractere = ','
string = input()
tamanho_string = len(string)
if ',' in  string:
    print('passed')
else:
    print('failed')
    

