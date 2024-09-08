def evaluar(caracter):

    ascii_valor = ord(caracter)
    respuesta = ""

    if 48 <= ascii_valor <= 57:
        respuesta = "Es número"
    elif 65 <= ascii_valor <= 90:
        respuesta = "Es letra mayúscula"
    elif 97 <= ascii_valor <= 122:
        respuesta = "Es letra minúscula"
    else:
        respuesta = "No es letra ni número"

    return respuesta

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)

