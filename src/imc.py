def evaluar(peso, estatura, edad):
    # Se calcula el índice de masa corporal
    imc = peso / (estatura ** 2)
    
    # Se aplican las condiciones para determinar el nivel de riesgo de enfermedades coronarias
    if edad < 45 and imc < 22:
        respuesta = "Bajo"
    elif edad < 45 and imc >= 22:
        respuesta = "Medio"
    elif edad >= 45 and imc < 22:
        respuesta = "Medio"
    elif edad >= 45 and imc >= 22:
        respuesta = "Alto"
    return respuesta

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
