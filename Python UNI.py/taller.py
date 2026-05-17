print("--- MENÚ DE OPERACIONES ---")
print("S: Suma")
print("R: Resta")
print("M: Multiplicación")
print("D: División")
letra = input("Ingrese la operacion que desea realizar: ").upper()
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
if letra == "S":
    print("La suma es:", n1 + n2)
elif letra == "R":
    print("La resta es:", n1 - n2)
elif letra == "M":
    print("La multiplicacion es:", n1 * n2)
elif letra == "D":
    print("La division es:", n1 / n2)

else:
    print("La letra que ingresaste no es correcta")