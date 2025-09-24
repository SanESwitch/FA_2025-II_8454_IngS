edad = int(input("Ingrese una edad: "))
print()
if edad >=18:
    print("Puede votar.")
    if edad >=25:
        print("Puede ser candidato a un cargo politiuco")
    else:
        print("No puede ser cantidato a un cargo politco")
else:
        print("No puede votar.")
