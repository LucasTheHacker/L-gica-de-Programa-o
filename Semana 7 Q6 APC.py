contador = 0 #define uma variável auxiliar para o loop while
soma_dos_dinheiros = 0 #define uma variável auxiliar para a soma dos valores
n_amigos, ingresso = map(int, input().split())

while contador != n_amigos:
    dinheiro_do_amigo = int(input()) #recebe os valores de cada amigo
    soma_dos_dinheiros += dinheiro_do_amigo #atualiza com a variável, somando o novo valor a ela
    contador += 1 #atualiza o contador pra não dar loop infinito
media = soma_dos_dinheiros//n_amigos

if media >= ingresso:
    print(f'media: {media:.0f}')
    print('o rock reinara mais uma vez')
else:
    print(f'media: {media:.0f}')
    print(f'rockeiros trabalhando ja')