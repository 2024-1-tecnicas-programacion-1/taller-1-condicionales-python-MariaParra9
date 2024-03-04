def evaluar(anno):
    abis = anno % 4
    if abis == 0:
        respuesta = str(anno) + " es bisiesto"
    else:
        respuesta = str(anno) + " no es bisiesto"
    return respuesta

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)