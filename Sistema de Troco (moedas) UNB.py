#Sistema de troco de supermercado: define a quantidade de moedas de 50, 25, 10, 5 e 1 centavos necessárias para dar o troco \n
#de forma a entregar o mínimo de moedas possíveis. É possível utilizar funções ou sequências de condicionais.
def troco(T):

    moedas_50 = T//50
    resto = T - moedas_50*50

    moedas_25 = resto//25
    resto2 = resto - moedas_25*25 

    moedas_10 = resto2//10
    resto3 = resto2 - moedas_10*10 

    moedas_5 = resto3//5 
    resto4 = resto3 - moedas_5*5

    moedas_1 = resto4//1
    resto5 = resto4 - moedas_1*1
    
    if T >= 50:
        print(f'{moedas_50} moedas de 50 centavos')  
    else:
        print('0 moedas de 50 centavos')

    if resto >=25:
        print(f'{moedas_25} moedas de 25 centavos')         
    else:
        print('0 moedas de 25 centavos')

    if resto2 >= 10:
        print(f'{moedas_10} moedas de 10 centavos')            
    else:
        print('0 moedas de 10 centavos')

    if resto3 >= 5:
        print(f'{moedas_5} moedas de cinco centavos')           
    else:
        print('0 moedas de cinco centavos')   

    if resto5 < 5:
        print(f'{moedas_1} moedas de 1 centavo')         
    else:
        print('0 moedas de 1 centavo')






