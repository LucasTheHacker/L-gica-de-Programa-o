num_inputs = int(input())
string = ''
dicionario = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
while num_inputs > 0:
    string = ''
    contador = 0
    comprimida = input()
    while contador < len(comprimida):
        if comprimida[contador].isdigit() ==False:
            if contador + 1 < len(comprimida) and contador + 2 < len(comprimida): #verificação pra não dar index out of range
                if comprimida[contador + 1].isdigit() == True and comprimida[contador + 2].isdigit() == True: 
                    multiplicador = 10*dicionario[comprimida[contador + 1]] + dicionario[comprimida[contador + 2]]
                    string += (comprimida[contador] * multiplicador)                   
        if contador + 1 < len(comprimida): 
            if contador + 2 < len(comprimida):
                if comprimida[contador + 2].isdigit() == True:
                    pass
                elif comprimida[contador].isdigit() == False:
                    multiplicador2 = dicionario[comprimida[contador + 1]]
                    string +=  (comprimida[contador]*multiplicador2)        
            elif comprimida[contador].isdigit() == False:
                if comprimida[contador + 1].isdigit() == True and comprimida[contador].isdigit() == False:
                    #if comprimida[contador + 2].isdigit() == False:
                    multiplicador2 = dicionario[comprimida[contador + 1]]
                    string +=  (comprimida[contador]*multiplicador2)
        contador += 1
    num_inputs -=1    
    print(string)   
