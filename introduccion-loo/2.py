""" 2. Leer dos valores enteros e informar la suma y su cociente """
""" En este caso agregamos la resta, producto y división"""

a = int(input("Ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))

print("La suma de los numeros ingresados es:", a + b)
print("La resta de los numeros ingresados es:", a - b)
print("El producto de los numeros ingresados es:", a * b)
print("La division entera de los numeros ingresados es:", a // b)
print(f"El cociente de los numeros ingresados es: {a / b:,.2f}")

""" int(input(...)): Usa input para capturar valores ingresados por el usuario y los convierte a enteros usando int

Hace todas las operaciones

Formato f-string: f"{a / b:,.2f}" formatea el resultado para mostrarlo con:
:,.2f: Incluye separadores de miles y muestra solo 2 decimales. """