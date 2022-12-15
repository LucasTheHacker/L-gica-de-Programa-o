#Questão 2
contador = 0 #define o contador 
salario_total = 0 #define uma variável pra armazenar a soma dos salários
while True:
    dados = input().split(",") #recebe os dados, criando uma lista com método ',' de sep.
    if dados[0] != 'Fim':
        contador += 1 #atualiza o contador
        salario = dados[1] #define quem é o salário na lista
        salario = float(dados[1]) #transforma o type de str pra float
        salario_total = salario_total + salario #atualiza a soma dos salários
    else:
        break
if contador == 0: #abrange o caso de não haver nenhum salário (division by zero)
    media = 0.00
else:
    media = salario_total/contador
print(f'{media:.2f}')