def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos
    if anno >= 1582:
        if anno % 400 == 0 or (anno % 4 == 0 and anno % 100 != 0):
            respuesta = f"{anno} es bisiesto"
        else:
            respuesta = f"{anno} no es bisiesto"
    else:
        if anno % 4 == 0:
            respuesta = f"{anno} es bisiesto"
        else:
            respuesta = f"{anno} no es bisiesto"

    return respuesta
            
if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
