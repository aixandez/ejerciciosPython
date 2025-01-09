""" 10. Desarrollar una función que muestre por pantalla los primeros n números naturales
considerando al 0 (cero) como primer número natural, siendo n un valor que se pasa por parámetro """

def mostrar_numeros_naturales(n):

    for i in range(n):
        print(i)

n = int(input("Ingrese la cantidad de números naturales a mostrar: "))
mostrar_numeros_naturales(n)
