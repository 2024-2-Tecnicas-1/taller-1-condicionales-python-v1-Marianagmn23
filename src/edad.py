from datetime import datetime
def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    current_date = datetime.now()
    nacimiento = datetime(anno, mes, dia)

    edad = current_date.year - nacimiento.year


    if (current_date.month < nacimiento.month) or (current_date.month == nacimiento.month and current_date.day < nacimiento.day):
        edad -= 1

    respuesta = "Usted tiene " + str(edad) + " años"
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
