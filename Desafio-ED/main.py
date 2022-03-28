fila1 = []
fila2 = []
fila3 = []
fila4 = []

a=0

while a==0:

    print("Número de pessoas em cada fila: ", len(fila1), " ", len(fila2), " ", len(fila3), " ", len(fila4), " ", )

    fila_numero = int(input("digite o número da sua fila (1, 2, 3 e 4): "))

    if fila_numero==1:
        horario_chegada = str(input("Digite a hora que você entrou na fila (hh:mm) - "))
        horario_saida = str(input("Digite a hora que você saiu na fila (hh:mm) - "))

        hora_chegada = int(horario_chegada.split(":")[0])
        minuto_chegada = int(horario_chegada.split(":")[1])
        hora_saida = int(horario_saida.split(":")[0])
        minuto_saida = int(horario_saida.split(":")[1])

        tempo_fila_h = (hora_saida - hora_chegada)
        string_h = repr(tempo_fila_h)
        tempo_fila_m = (minuto_saida - minuto_chegada)
        string_m = repr(tempo_fila_m)
        tempo_final = ("Tempo final foi de " + string_h + " hora(s) e " + string_m + " minutos")
        print(tempo_final)

        a = int(input("Digite 0 para confirmar entrada na fila e continuar o processo: "))

        fila1.append(tempo_fila_m)

    elif fila_numero==2:

        horario_chegada = str(input("Digite a hora que você entrou na fila (hh:mm) - "))
        horario_saida = str(input("Digite a hora que você saiu na fila (hh:mm) - "))

        hora_chegada = int(horario_chegada.split(":")[0])
        minuto_chegada = int(horario_chegada.split(":")[1])
        hora_saida = int(horario_saida.split(":")[0])
        minuto_saida = int(horario_saida.split(":")[1])

        tempo_fila_h = (hora_saida - hora_chegada)
        string_h = repr(tempo_fila_h)
        tempo_fila_m = (minuto_saida - minuto_chegada)
        string_m = repr(tempo_fila_m)
        tempo_final = ("Tempo final foi de " + string_h + " hora(s) e " + string_m + " minutos")
        print(tempo_final)

        a = int(input("Digite 0 para confirmar entrada na fila e continuar o processo: "))

        fila2.append(tempo_fila_m)

    elif  fila_numero==3:

        horario_chegada = str(input("Digite a hora que você entrou na fila (hh:mm) - "))
        horario_saida = str(input("Digite a hora que você saiu na fila (hh:mm) - "))

        hora_chegada = int(horario_chegada.split(":")[0])
        minuto_chegada = int(horario_chegada.split(":")[1])
        hora_saida = int(horario_saida.split(":")[0])
        minuto_saida = int(horario_saida.split(":")[1])

        tempo_fila_h = (hora_saida - hora_chegada)
        string_h = repr(tempo_fila_h)
        tempo_fila_m = (minuto_saida - minuto_chegada)
        string_m = repr(tempo_fila_m)
        tempo_final = ("Tempo final foi de " + string_h + " hora(s) e " + string_m + " minutos")
        print(tempo_final)

        a = int(input("Digite 0 para confirmar entrada na fila e continuar o processo: "))

        fila3.append(tempo_fila_m)

    elif fila_numero==4:

        horario_chegada = str(input("Digite a hora que você entrou na fila (hh:mm) - "))
        horario_saida = str(input("Digite a hora que você saiu na fila (hh:mm) - "))

        hora_chegada = int(horario_chegada.split(":")[0])
        minuto_chegada = int(horario_chegada.split(":")[1])
        hora_saida = int(horario_saida.split(":")[0])
        minuto_saida = int(horario_saida.split(":")[1])

        tempo_fila_h = (hora_saida - hora_chegada)
        string_h = repr(tempo_fila_h)
        tempo_fila_m = (minuto_saida - minuto_chegada)
        string_m = repr(tempo_fila_m)
        tempo_final = ("Tempo final foi de " + string_h + " hora(s) e " + string_m + " minutos")
        print(tempo_final)

        a = int(input("Digite 0 para confirmar entrada na fila e continuar o processo: "))

        fila4.append(tempo_fila_m)





media_fila1 = (sum(fila1))/(len(fila1))
media_fila2 = (sum(fila2))/(len(fila2))
media_fila3 = (sum(fila3))/(len(fila3))
media_fila4 = (sum(fila4))/(len(fila4))

print("A fila 1 teve uma média de ",media_fila1)
print("A fila 2 teve uma média de ",media_fila2)
print("A fila 3 teve uma média de ",media_fila3)
print("A fila 4 teve uma média de ",media_fila4)