""" 3. Dado un valor numérico entero, informar si es par o impar """

a = input('Ingrese un valor entero: ')

if int(a) % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")

    """ El input pide que el usuario ingrese por teclado
     El int(a) convierte el texto ingresado a un número entero """
    
    """ int(a) % 2: Calcula el resto de dividir el número entre 2:
     
        Si el resto es 0, significa que el número es divisible entre 2, por lo que es par.
       
        Si el resto es distinto de 0, el número es impar. """