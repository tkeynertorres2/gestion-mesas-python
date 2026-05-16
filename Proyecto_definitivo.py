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
#Fecha para la facturacion
import datetime
ahora=datetime.datetime.now()
h_ordenada=ahora.strftime("%d/%m/%Y")
#Carta enumerada y con precios 
def mostrar_carta():
       print(f"=====================\n🍽️  SABORES DEL LLANO 🍽️\n=======================")
       for i in range(len(carta)):
            print(f"{i+1} {carta[i][1]:30} -$- {carta[i][2]:,}")
#una lista dentro de una lista con enumeracion 
añadidos=[[] for _ in range(10)]    

#Opciones para el cliente
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

    #Por si añaden letra en vez del numero no rompa el codigo 
    while True:
     try: 
       opcion=int(input("Ingrese el número de la opción necesaria:" " "))
       break
     except:
         print("❌ Opción inválida, vuelva a intentarlo")

    if opcion==1:
        mostrar_carta()
        
    #Añadir arreglos con try y while true, para que no rompan el codigo 
    elif opcion==2:
      while True:
          try:
           N_mesa=int(input("Ingrese el número de mesa (1-10): " ""))
           break
          except:
              print("❌ Opción inválida, vuelva a intentarlo")
              
      agregar_mas_productos=True 
      
      while agregar_mas_productos:
          while True:
              try:
               producto=int(input("Ingrese el número de producto que desea agregar: " ""))
               break
              except:
                  print ("❌ Opción inválida, vuelva a intentarlo")
                  
          añadidos[N_mesa-1].append(producto-1)
          decision=input ("¿Desea agregar otro producto? (Si/No): " "").lower().strip()
          if decision =="si":
              continue
          elif decision=="no":
            agregar_mas_productos=False
            break
          else:
              print ("❌ Opción inválida, escriba (Si/No)")
         
    elif opcion==3:
      eliminar_producto=True
      while True:
       try: 
         N_mesa=int(input("Ingrese el número de la mesa (1-10):" " "))     
         break 
       except:
            print("❌ Opción inválida, vuelva a intentarlo")
      while eliminar_producto:
       while True:
         try:
          print("---Lista---")
          if len(añadidos[N_mesa-1])==0:
              print ("No hay pedidos en la mesa")
              break
          for i,idx in enumerate(añadidos[N_mesa-1]):
              print (f"{i+1}.{carta[idx][1]}  $ {carta[idx][2]:,}")
          no_producto=int(input("Ingrese el número del producto que desea eliminar: " ""))
          añadidos[N_mesa-1].pop(no_producto-1)
          print ("✅ Producto eliminado correctamente")
          decision=input ("¿Desea eliminar otro producto? (Si/No)").lower().strip()
          if decision=="si":
              añadidos
          elif decision=="no":
                   eliminar_producto=False
                   break
          else:
              print ("❌ Opción inválida, escriba (Si/No)")
         except:
            print("❌ Opción inválida, vuelve a intentarlo") 
    elif opcion==4:
            N_mesa=int(input("Ingrese el número de la mesa (1-10): " ""))
            print("Productos pedidos:")
            for idx in añadidos[N_mesa-1]:
                print (f"{carta [idx][0]}{carta [idx][1]} -$- {carta[idx][2]:,}")
        
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
          break
         except:
            print ("❌ Opción inválida, vuelve a intentarlo")
        print (f"""\n--|Sabores del Llano|--\n
               {h_ordenada}
               ---------mesa: {N_mesa}
               Dia: {dia_descuento}
               Productos consumidos:""")
        for idx in añadidos[N_mesa-1]:
           print (f"{(carta[idx][1])} precio: {(carta[idx][2]):,}")
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
