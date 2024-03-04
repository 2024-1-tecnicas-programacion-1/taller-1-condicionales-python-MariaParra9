from datetime import date

def evaluar(dia, mes, anno):
    fecha_actual = date.today()
    dia_actual = fecha_actual.day
    mes_actual = fecha_actual.month
    anno_actual = fecha_actual.year
    edad = anno_actual - anno
    
    if mes == mes_actual:
        if dia == dia_actual:
            respuesta = "Usted tiene " + str(edad) + " años"
        elif dia < dia_actual:
            respuesta = "Usted acaba de cumplir " + str(edad) + " años"
        else:
            respuesta = "Usted acaba de cumplir " + str(edad) + " años"
    elif mes < mes_actual:
        if dia == dia_actual:
            respuesta = "Cumpliste " + str(edad) + " años"
        elif dia < dia_actual:
            respuesta = "Cumpliste " + str(edad) + " años"
        else:
            respuesta = "Cumpliste " + str(edad) + " años"
    elif mes > mes_actual:
        if dia == dia_actual:
            respuesta = "Vas a cumplir " + str(edad) + " años"
        elif dia < dia_actual:
            respuesta = "Vas a cumplir " + str(edad) + " años"
        else:
            respuesta = "Vas a cumplir " + str(edad) + " años"
        
    return respuesta

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
