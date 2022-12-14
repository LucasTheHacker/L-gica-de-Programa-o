salarios = [0] #cria uma lista com um valor para caso não haja nenhum salário
while True:
    dados = input().split(sep=',') #Recebe os dados usando o método sep com a vírgula
    if dados[0] != 'Fim':
        salario_unico = float(dados[1]) #declara a variável para o salário
        salarios.append(salario_unico) #adiciona o salário à lista 'vazia' criada anteriormente
    else:
        break #sai do loop infinito
maior_salario = max(float(salario_unico) for salario_unico in salarios) #calcula o maior valor de ponto flutuante para as variáveis 'salário_unico' na lista 'salarios'
if maior_salario == 0: 
    print('Não tem') #condição imposta pela questão
else:
    print(f'{maior_salario:.2f}') #f string com 2 casas de ponto flutuante
      
        
    
    

