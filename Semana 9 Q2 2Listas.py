num_inputs = int(input())
usernames = []
crewmates = []    
for i in range(num_inputs):
    nome_de_usuario = input()
    usernames.append(nome_de_usuario)
if num_inputs == 1:
    print(*usernames) #printa somente a string que entrou
else:
    impostores = input().split(sep=' ')
    for i in range(len(usernames)):
        if usernames[i] not in impostores:  #se o username não estiver em impostores, adiciona a crewmates
            crewmates.append(usernames[i])          
    print(*crewmates)
        
    