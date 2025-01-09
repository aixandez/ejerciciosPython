""" 8. Se ingresa por teclado un conjunto de valores numéricos enteros positivos,
se pide informar, por cada uno, si el valor ingresado es par o impar.
Para indicar el final se ingresará un valor cero o negativo """

v = int(input("Ingrese un valor entero positivo: "))
while v > 0:
    if v % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
    v = int(input("Ingrese un valor entero positivo: "))

print("Fin")

""" Se le pide al usuario un valor entero positivo

Mientras el valor sea mayor a cero se ejecuta un buble while

El bucle verifica la paridad

Despues de verificar pide al usuario que ingrese otro valor

Cuando se ingresa 0 o menos, el bucle termina e imprime "Fin" """