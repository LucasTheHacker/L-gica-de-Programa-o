#Retorna os elementos da lista que tem número par de vogais
#chamada
#print(paron(['todos', 'nos', 'adoramos', 'disciplina', 'apc']))

casox = '[]'
def paron(lista): 
    paronicas = []
    global casox
    lista = list(lista)
    if lista == []:
        return casox
    else:
        for i in range(len(lista)): #cada palavra da lista
            contador = 0
            for a in range(len(lista[i])): #cada letra de cada palavra da lista
                palavra = str(lista[i])  #palavra = palavra da lista no momento
                if palavra[a] in 'aeiouAEIOU': #se a letra do índice atual for vogal
                    contador += 1 #atualizo minha quantidade de vogais
                    #volto pro loop for pra palavra atual
            if contador%2 == 0: #checko se o contador é par
                paronicas.append(lista[i])
        return paronicas
