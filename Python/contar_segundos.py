def contar_segundos(segundos):
    dias = segundos // 86400
    segs_restantes = segundos % 86400
    horas = segs_restantes // 3600
    segs_restantes = segs_restantes % 3600
    minutos = segs_restantes // 60
    segs_restantes_final = segs_restantes % 60

    if dias > 0:
        print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final,\
     "segundos.")

    elif horas > 0:
        print(horas, "horas,", minutos, "minutos e", segs_restantes_final,\
     "segundos.")

    else:
        print(minutos, "minutos e", segs_restantes_final,\
     "segundos.")