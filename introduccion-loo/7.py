""" 7. Leer un valor numérico que representa un día de la semana.
Se pide mostrar por pantalla el nombre del día considerando que el lunes es el día 1, el martes es el día 2 y así, sucesivamente """

dia = int(input("Ingrese un número entre 1 y 7 que represente un día de la semana: "))

if dia == 1:
    print("lunes")
elif dia == 2:
    print("martes")
elif dia == 3:
    print("miércoles")
elif dia == 4:
    print("jueves")
elif dia == 5:
    print("viernes")
elif dia == 6:
    print("sábado")
elif dia == 7:
    print("domingo")
else:
    print("número inválido, ingrese un número del 1 al 7")