#População de A sempre menor que a de B
dados = input().split(sep=' ') #só pra treinar a utilização de listas e ficar mais legível o código
pop_A = int(dados[0])
pop_B = int(dados[1])
taxa_A = float(dados[2])
taxa_B = float(dados[3])
crescimento_A = 0
crescimento_B = 0
controle = 0 #variável auxiliar de controle do tempo
if taxa_A < taxa_B:
    print('A nunca alcancara B.')    
else:
    while pop_A < pop_B and controle < 1000: # Coloquei uma nova condição pra quando passar de 1000 anos, o erro é que os valores estavam ficando muito grande nos testes escondidos eté um momento que não dava mais pra converter pra inteiro
        crescimento_A = int((pop_A * (taxa_A/100))) #calcula a parte inteira da nova população com o passar de um ano
        crescimento_B = int((pop_B * (taxa_B/100))) #converte pra inteiro; evitando a mensagem de erro
        pop_A += crescimento_A
        pop_B += crescimento_B
        #OverFlowError: cannot convert float infinity to integer
        #OverFlowError: Int too large to convert to float
        controle += 1 #Se a variável de controle do tempo for atualizada após as condicionais, sempre dará 1 ano a menos
    if controle >= 1000:
        print('Mais de um milenio.')
    else:
        print(f"Vai alcancar em {controle} ano(s).")         
#if taxa_A == 0:
#    print('A nunca alancara B')
#elif taxa_A <= taxa_B: #Esse if impede que se utilize memória demasiada no loop true
#    print('A nunca alcancara B.')
#elif controle <= 1000:
#    print(f"Vai alcancar em {controle} ano(s).") 
#else:
#    print('Mais de um milenio')
        
        
    