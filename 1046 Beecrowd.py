#1045 Beecrowd
t_inicial, t_final = map(int, input().split())
if  t_inicial < t_final:
    print(f'O JOGO DUROU {t_final - t_inicial} HORA(S)')
elif t_inicial == t_final:
    print(f'O JOGO DUROU 24 HORA(S)')
else: #caso o tempo comece em um dia e termine em outro
    d1 = 24 - t_inicial
    d2 = t_final
    tempox = d1 + d2
    print(f'O JOGO DUROU {tempox} HORA(S)')
