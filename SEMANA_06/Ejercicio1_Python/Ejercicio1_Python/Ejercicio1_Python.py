num = int(input("Ingrese entero mayor a 0: "))

while num<=0:
    num = int(input("Error. Ingrese entero mayor a 0; "))

i = 1 #valor inicial
print()

while i<=12:
    print(f"{num} x {i} = {num*i}")
    i+=1
