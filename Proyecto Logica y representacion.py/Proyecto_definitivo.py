#Diccionario con la carta del restaurante, con el numero del producto, su nombre y su precio
carta=[["1.", "Carne a la llanera ",40000],
      ["2.", "Mamona",28000],
      ["3.","Sobrebarriga asada",27000],
      ["4.","Costillas BBQ",45000],
      ["5.","Churrasco",35000],
      ["6.","Pechuga a la plancha",20000],
      ["7.","Hamburguesa artesanal", 18000],
      ["8.","Perro caliente especial", 14000],
      ["9.","Arepa con queso", 8000],
      ["10.","Patacon con carne",16000],
      ["11.","Salchipapa mixta", 19000], 
      ["12.","Cerveza", 7000],
      ["13.","Jugo natural", 6500],
      ["14.","Jarra de limonada",8000],
      ["15","Agua",4000]]
#fecha y hora actual para la factura
import datetime
ahora=datetime.datetime.now()
h_ordenada=ahora.strftime("%d/%m/%Y")
#Carta enumerada y con precios 
def mostrar_carta():
       print(f"=====================\n🍽️  SABORES DEL LLANO 🍽️\n=======================")
       for i in range(len(carta)):
            print(f"{i+1} {carta[i][1]:30}  $ {carta[i][2]:,}")
#lista de listas para almacenar los productos añadidos a cada mesa, con 10 mesas disponibles
añadidos=[[] for _ in range(10)]    

#opciones del menu con validacion de entradas
def menu():
   opcion=0
   while opcion !=6 :
    print("\n MENÚ PRINCIPAL")
    print("-"*25)
    print ("""
     1.📋 Carta
     2.➕ Añadir producto
     3.❌ Eliminar producto
     4.👀 Ver pedido de la mesa 
     5.🧾 Factura 
     6.🚪 Salir""")

#Elección de opciones con try para que no rompa el codigo 
    while True:
     try: 
       opcion=int(input("\nIngrese el número de la opción necesaria:" " "))
       break
     except ValueError:
         print("❌ Opción inválida, vuelva a intentarlo")
#mostrar carta
    if opcion==1:   
        mostrar_carta()
        
#Añadir productos a la mesa y posibilidad de añadir mas de un producto
    elif opcion==2:
      while True:
          try:
           print("\n "+"═══"*25)
           N_mesa=int(input("Ingrese el número de mesa (1-10): " ""))
           print ("═══"*25)
           if N_mesa<1 or N_mesa>10:
               print("❌ Opción inválida, Ingrese un número entre 1 y 10")
               continue
           else:
            break
          except ValueError:
              print("❌ Opción inválida, vuelva a intentarlo")
#true para que se repita hasta que sea false y se deje de agregar productos a la mesa
      agregar_mas_productos=True 
#validacion de producto a agregar y posibilidad de agregar mas productos a la mesa
      while agregar_mas_productos:
          while True:
              try:
               producto=int(input("Ingrese el número de producto que desea agregar: " ""))
               print ("✅ Producto agregado correctamente")
               print ("═══"*25)
               if producto<1 or producto>15:
                    print("❌ Opción inválida, Ingrese un número entre 1 y 15")
                    continue
               else:
                break
              except ValueError:
                  print ("❌ Opción inválida, vuelva a intentarlo")
#lista con la variable de los productos añadidos 
          añadidos[N_mesa-1].append(producto-1)
#while para que no se rompa el codigo cuando se ingrese una opción diferente a si o no.
          while True:
               decision=input ("¿Desea agregar otro producto? (Si/No): " "").lower().strip()
               print ("═══"*25)  
               if decision =="si" or decision=="shi" or decision=="s" or decision=="sip"   :
                break
               elif decision=="no" or decision=="noo" or decision=="n" or decision=="nop":
                agregar_mas_productos=False
                break
               else:    
                print ("❌ Opción inválida, escriba (Si/No) \n---------------------------------------------")
                
                continue

    elif opcion==3:
     eliminar_producto=True
     while eliminar_producto:
    #seguro para que no se rompa el codigo cuando ingresen un numero de mesa diferente a 1-10 o una letra.   
        try: 
         print("\n "+"═══"*25)
         N_mesa=int(input("Ingrese el número de la mesa (1-10):" " "))   
         if N_mesa<1 or N_mesa>10:
            print("❌ Opción inválida, Ingrese un número entre 1 y 10")
            continue
         print ("═══"*25)    
         break
        except ValueError:
            print("❌ Opción inválida, vuelva a intentarlo")
            continue 
#while para eliminar productos de la mesa.
      
     while True:
#seguro para que ingresen la opcion corrrecta y no se rompa eol codigo cuando no hay productos 
         try:
          print("---Lista---")
          if len(añadidos[N_mesa-1])==0:
              print ("No hay pedidos en la mesa")
              eliminar_producto=False   
              break
#enumerar los productos añadidos a la mesa para que el usuario pueda elegir cual eliminar
          for i,idx in enumerate(añadidos[N_mesa-1]):
              print (f"{i+1}.{carta[idx][1]:20}  $ {carta[idx][2]:,}")

          print ("═══"*25)
#limitandon los numeros de producto a eliminar.
          no_producto=int(input("Ingrese el número del producto que desea eliminar: " ""))
          if no_producto<1 or no_producto>len(añadidos[N_mesa-1]):
              print("═══"*25)
              print("═══ ❌ Opción inválida, Ingrese un número de los productos añadidos.═══")
              continue
#quitar el producto añadido.
          añadidos[N_mesa-1].pop(no_producto-1)
          print ("✅ Producto eliminado correctamente")
          print ("═══"*25)  
          
          while True:
           decision=input ("¿Desea eliminar otro producto? (Si/No)").lower().strip()
           if decision=="si" or decision=="shi" or decision=="s" or decision=="sip"   :
              break 
             
           elif decision=="no" or decision=="noo" or decision=="n" or decision=="nop":
                   eliminar_producto=False
                   break
           else:    
              print ("❌ Opción inválida, escriba (Si/No)")
              print ("═══"*25) 
          if not eliminar_producto:
              break 

         except ValueError:
            print("❌ Opción inválida, vuelve a intentarlo") 
            continue
         print ("═══"*25)  
    elif opcion==4:
            print ("═══"*25)
            N_mesa=int(input("\n Ingrese el número de la mesa (1-10): " ""))
            print ("═══"*25)    
            print("Productos pedidos:")
            for i, idx in enumerate(añadidos[N_mesa-1]):
                print (f"{i+1}.  {carta [idx][1]:20}  $ {carta[idx][2]:,}") 
                print ("------"*25)  
        
#Factura (aun no terminada falta acomodar todo lo de abajo) 
##FALLOS:no da bien los productos consumidos y faltan mas detallitos, e incluso el total    
    elif opcion==5:
        subtotal=0
        ##El dia con la fecha real para que este sea mas automatizado  y no se tenga que hacer un input pidiendo el dia (NO SE A VERIFICADO SU FUNCIONAMIENTO)
        dia=ahora.strftime("%A")
        dias_traducidos={"Monday":"Lunes",
                           "Tuesday":"Martes",
                           "Wednesday":"Miércoles",
                           "Thursday":"Jueves",
                           "Friday":"Viernes",
                           "Saturday":"Sábado",
                           "Sunday":"Domingo"}
        dia_descuento=dias_traducidos[dia]
        suma=0
        while True:
         try:
          N_mesa=int(input("Ingrese el número de la mesa que desea la factura (1-10): " "" ))
          if N_mesa<1 or N_mesa>10:
              print("❌ Opción inválida, Ingrese un número entre 1 y 10")
              continue
          break
         except ValueError:
            print ("❌ Opción inválida, vuelve a intentarlo")
        print (f"""\n--|Sabores del Llano|--\n{h_ordenada}\nmesa: {N_mesa}\nDia: {dia_descuento}
               Productos consumidos:""")
        for idx in añadidos[N_mesa-1]:
           print (f"{(carta[idx][1]):20} precio: {(carta[idx][2]):,}")
           ##Dentro del for pq si no vuelve a botar error debido a que no se reproduce el idx
           subtotal+=carta[idx][2]
        print (f"Subtotal: {subtotal:,}")
        if dia_descuento in ["Lunes","Martes","Miércoles"]:
            descuento=subtotal*0.10
            total=subtotal-descuento
            print(f"total:{total:,}")
        else: 
            total=subtotal
            print (f"💵 Total:{total:,}")
        añadidos[N_mesa-1].clear()
##Recordatorio(Liberacion de mesa)
    elif opcion==6:
          print("Mesa liberada,saliendo del sistema")
    else:
        print("❌ Opcion invalida ")
menu()
## contar y contador para hacer el producto mas vendido 
