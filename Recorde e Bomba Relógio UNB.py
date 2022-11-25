tempo_explosao = int(input())
tempo_recorde = int(input())
def contagemregressiva(tempo_explosao):

    if tempo_explosao == 0:
        print('Cabum!!!! Explodiu')
    else:
        if tempo_explosao == 5:
            print('Seu tempo está acabando')
            contagemregressiva(tempo_explosao-1)
        elif tempo_explosao == 1:
            if tempo_explosao > tempo_recorde:
                print('Seja rápido. Falta 1 segundo')
            elif tempo_explosao < tempo_recorde:
                print( 'Bomba desativada automaticamente!' )
            contagemregressiva(tempo_explosao-1)
            
        else:
            print(f'Atenção faltam {tempo_explosao} segundos...')                 
            contagemregressiva(tempo_explosao-1)

contagemregressiva(tempo_explosao)




