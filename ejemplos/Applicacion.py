edad = int(input("Digite su edad:"))

if edad >= 18:
    num1 = int(input("Ingrese primer valor:"))

    num2 = -1
    while num2 == -1:
        try:
            num2 = int(input("ingrese segundo valor:"))
        except:
            num2 = -1
            print("Los valores de entrada solo son numericos.")

    suma = num1 + num2
    producto = num1 * num2
    print("La suma de los dos valores es")
    print(suma)
    print("El producto de los dos valores es")
    print(producto)
else:
    print("Debes ser mayor de edad para usar la aplicación.")

for taco in range(1, 10):
    print("Taco: "+str(taco))

