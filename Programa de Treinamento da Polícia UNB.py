#Problemas enfrentados: referenciar variável global; erro de global and parameter; referenciar variável prior global;
#Desafio de algoritmo: Programa para o treinamento antibomba da polícia.
#Entrada: consiste em duas linhas, a primeira com o tempo em segundos, entre 0 e 100, que o policial tem para desativar
#O segundo input se refere ao tempo recorde do policial, entre 0 e 100.
#são apresentadas uma série de restrições com base nas relações entre os tempos.
tempo_explosao = int(input())
tempo_recorde = int(input())
explosao = tempo_explosao
recorde = tempo_recorde
def contagemregressiva(tempo_explosao):

    global recorde
    global explosao

    if tempo_explosao == 0:
        print('Cabum!!!! Explodiu')
    else:
        if tempo_explosao == 5:
            print('Seu tempo está acabando!')
            contagemregressiva(tempo_explosao-1)
        elif tempo_explosao == 1 and explosao > recorde:       
                print('Seja rápido. Falta 1 segundo')
                contagemregressiva(tempo_explosao-1)
        elif tempo_explosao == 1 and explosao <= recorde:   
                print('Bomba desativada automaticamente!')           
        else:
            print(f'Atenção faltam {tempo_explosao} segundos...')                 
            contagemregressiva(tempo_explosao-1)

contagemregressiva(tempo_explosao)



