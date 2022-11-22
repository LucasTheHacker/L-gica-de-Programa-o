#Esse programa executa, por meio de pensamento computacional, uma série de condicionais aninhadas.
#Também é possível fazer o programa utilizando uma função recursiva e o operador 'elif'.
#A instrução para esse desafio está em uma foto que descreve uma pergunta base e diversas frases que podem ser feitas baseadas em SIM ou NAO.
funciona = input('O programa funciona?\n')

if funciona == 'SIM':      
    entende = input('Você entende o que fez?\n')    
    if	 entende == 'SIM':        
                print('Ótimo. Então não mexe!\n')                
    else:
        tutoria = input('Já foi na tutoria?\n')
        if tutoria == 'SIM':            
            print('Choremos!\n')
        else:
            print('Temos um time a disposição!\n')            
else:    
    erro = input('Você sabe onde está o erro?\n')    
    if erro == 'NÃO':        
        tutoria = input('Já foi na tutoria?\n')
        if tutoria == 'SIM':
            print('Choremos!\n')
        else:
            print('Temos um time a disposição!\n')            
    else:        
        sozinho = input('Acha que pode solucionar sozinho?\n')
        if sozinho == 'SIM':
            print('Então mão na massa!\n')            
        else:           
            google = input('Já pesquisou no Google?\n')
            if google == 'SIM':
                tutoria = input('Já foi na tutoria?\n')
                if tutoria == 'SIM':
                    print('Choremos!\n')
                else:
                    print('Temos um time a disposição!\n')                    
            else:
                print('Corre lá então!\n')
                    
                                
                    
                        
                
                
            
