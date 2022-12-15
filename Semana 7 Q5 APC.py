menor_nome = '' #definição de variáveis auxiliares
maior_nome = ''
menor_salario = 0
maior_salario = 0
soma_salarial = 0
contador = 0
tamanho = int(input())

if tamanho == 0: #caso para caso não haja tamanho
    print('Não tem média')
    print('Não tem')
    print('Não tem')
else:
    while contador != tamanho:        
        dados = input().split(sep=",") #cria uma lista 'dados'
        nome = dados[0] #primeiro elemento da lista é o nome, type str
        salario = float(dados[1]) #segundo elemento da lista é o salario, type float
        soma_salarial += salario #variável de soma dos salários, soma todos os valores de salário que entram
        if salario < menor_salario or  menor_salario == 0: #se o salario que entrar for menor que o menor_salario ou o menor_salario for zero
            menor_salario = salario #atualiza o valor da variável menor salário
            menor_nome = nome #atualiza o valor da variável menor_nome, que vem junto com o loop que veio o menor salário
        if salario > maior_salario: #caso o salario de entrada seja maior que o maior_salario
            maior_salario = salario #atualiza maior_salario do salario do loop 
            maior_nome = nome #atualiza o nome do maior_salario, que vem junto com o maior_nome
        contador += 1 #atualiza o contador(consome menos memória e processamento que o while True)
        
if tamanho != 0: #Caso de haver tamanho, para não dar division by zero
    media = soma_salarial/tamanho
    print(f'{media:.2f}')
    print(f'{maior_nome} {maior_salario:.2f}')
    print(f'{menor_nome} {menor_salario:.2f}') 


    
    
    
    