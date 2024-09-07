def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Division

    if residuo == 0:
        respuesta = (f"La división es exacta.\n"
                     f"Cociente: {cociente}\n"
                     f"Residuo: {residuo}")
    else:
        respuesta = (f"La división no es exacta.\n"
                     f"Cociente: {cociente}\n"
                     f"Residuo: {residuo}")
    
    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
