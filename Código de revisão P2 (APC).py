#Fazendo fatorial com função recursiva
########################################
#ALGORITMO GERAL P/ FUNÇÕES RECURSIVAS
#define um caso base pra sua função ir atrás, se não a função vai dar time limit e não vai funcionar
########################################
def fatorial(n):
    if n == 0:
        return 1    #função com resultado impede que retorne None, porque ele é uma instância na memória ram, e não a manipulação de uma instância
    elif n == 1:
        return 1
    else:
        return n * fatorial(n-1)  #imaginando que o número que entrou foi 2
    # então, vai retornar 2 *fatorial (2-1), so que o fatorial de (2-1) retorna 1
    #   então, vai retornar 2*1
    # a mesma coisa pros outros
    
#Exemplo de funçaõ recursiva com resultado --> QUESTÃO 6 SEMANA DE CONDICIONAIS E RECURSIVIDADE

def imprimeTermos(n):  #aqui, não temos que fazer operações com a instância (valor atual de uma variável), portanto ela não assume nenhum valor
    #apenas printa um termo e atualiza qual termo deve ser printado na sequência
    if n <= 0:
        print(0)
    else:
        print(n)
        imprimeTermos(n-2)
        
        
###########################
#Fazendo essas questões utilizando iteração
###########################
#n = int(input())
if n <= 1 and n >= 0:
    fatorial = 1
    print(fatorial)
else:
    for i in range(n):   # O i vai de zero até n
        if i > 0:         #se o i = 0 entrasse no cálculo, daria tudo zero
            n = n*i       #atualiza o valor da variável com a multiplicação pelo termo -1
    print(n)

#############################
#Progressão aritmética utilizando função com resultado
#############################
def termo_n(i, r, n):
    An = i + (n-1)*r  #Termo geral é igual ao primeiro termo vezes a multiplicaçãop da razão pelo enésimo termo decrementado em 1
    return An  #Retorna uma instância 

############################
#Sequência de Dêivis
############################
#A lógica dessa é a soma dos dois termos anteriores menos 1
def sequencia_deiviana(n):
    if n == 1:
        return 1 
    elif n == 2:
        return 2
    else:
        return ((sequencia_deiviana(n-1) + sequencia_deiviana(n-2)) - 1 )
#a lógica dessa recursividade é que o primeiro n com valor será o terceiro, que vai ser a soma de 1 + 2 - 1 = 2
#A partir daí, já se sabe qual o valor desse termo para o próximo e assim por diante

###########################
#Revisão de iteração --> Funções de primos
###########################
def ehPrimo(n):
    for i in range(n):   #i vai de 0 até o número
        if i > 1 and i < n:  #os valores que a gente quer são os os maiores do que 1, porque toda divisão por 1 tem resto = 0, e menor do que o próprio número, pois toda divisão de um número por si mesmo tem resto zero
            resto = n%i   #calculo da divisão pelo i em questão
            if resto == 0:  #se a divisão por esse i em questão tiver resto = 0, não é primo, pois é divisível por esse valor de i
                return 0
    return 1  #se terminar o loop for e não retornar 0, ele retorna o 1, pois o 0 não foi ativado (trigger)
def divisoresPrimos(d):  #usando a mesma lógica pra calcular a quantidade de divisores primos, so que utilizando um contador
    contador = 0 
    for i in range(d):
        if i > 1 and i < d: #mesma lógica do primeiro if da função acima
            resto = d%i   #mesma lógica
            if resto == 0:  #se for divisível, isto é, resto == 0, então eu pego esse valor de i em questão, pois temos um divisor
                if ehPrimo(i) == 1:  #chamo a função é ehPrimo para esse i atual e verifico se é True
                    contador += 1 # se for True, então temos um divisor primo
    return contador