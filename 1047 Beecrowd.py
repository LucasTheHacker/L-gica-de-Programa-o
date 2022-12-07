#1047 Beecrowd
hi, mi, hf, mf = map(int, input().split())
if mi < mf and hi < hf: #6:10 às 9:40
    horas = hf - hi
    minutos = mf - mi
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
elif mi == hi == hf == mf:
    print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif hi == hf and mi < mf:
    tempo = mf - mi
    print(f'O JOGO DUROU 0 HORA(S) E {tempo} MINUTO(S)')
elif hi < hf and mf < mi: #Exemplo: 7:10 às 8:09
    hi_minutos = hi * 60
    hf_minutos = hf * 60
    inicial_total = hi_minutos + mi
    final_total = hf_minutos + mf
    delta_minutos = final_total - inicial_total
    horas = delta_minutos//60
    minutos = delta_minutos%60
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
elif hi > hf and mi < mf:
    horas_dia1 = 24 - hi
    horas_total = horas_dia1 + hf
    minutos_total = mf - mi
    print(f'O JOGO DUROU {horas_total} HORA(S) E {minutos_total} MINUTO(S)')
else:
    minutos_do_dia = 24*60
    minutos_dia1 = (hi*60) + mi
    minutos_dia2 = (hf*60) + mf
    minutos_dia1_res = minutos_do_dia - minutos_dia1 #calcula o tempo até 00:00
    tempo_total_minutos = minutos_dia1_res + minutos_dia2
    #convertendo o tempo total para horas e minutos
    horas = tempo_total_minutos//60
    minutos = tempo_total_minutos % 60
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
