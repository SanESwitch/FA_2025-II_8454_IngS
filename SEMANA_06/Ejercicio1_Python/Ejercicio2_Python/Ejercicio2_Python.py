sumaP = sumaI = 0

while True:
    num=int(input("Ingrese numero (0 salir): "))

    if(num==0):
        break

    if(num<0):
        print("Error. Ingrese un numero negativo!")
        continue

    if num%2 ==0:
        sumaP+=num
    else:
        sumaI+=num

print("\nSuma de pares: ",sumaP)
print("Suma de impares: ",sumaI)