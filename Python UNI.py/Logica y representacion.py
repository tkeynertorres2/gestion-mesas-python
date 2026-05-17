n1=float(input("Ingrese La primera nota:"))
n2=float(input("Ingrese La segunda nota:"))
n3=float(input("Ingrese La tercera nota:"))
suma=n1+n2+n3
definitiva=suma/3
mensaje=f"Bien su defintiva es {definitiva}" if definitiva>=3 else f"Sobresliente, su defintiva es: {definitiva}" if definitiva >=4 else f"Excelente, su definitiva es {definitiva}" if definitiva==5 else f"Insuficiente su definitva es: {definitiva}" if definitiva<3