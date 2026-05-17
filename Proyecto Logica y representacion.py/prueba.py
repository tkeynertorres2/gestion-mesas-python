# ==========================================================
# 🍽️ SABORES DEL LLANO 🍽️
# Sistema de pedidos y facturación
# ==========================================================

import datetime
from collections import c

# ==========================================================
# CONSTANTES
# ==========================================================

NUM_MESAS = 10
DESCUENTO = 0.10
DIAS_DESCUENTO = ["Lunes", "Martes", "Miércoles"]

# ==========================================================
# CARTA DEL RESTAURANTE
# [nombre, precio]
# ==========================================================

carta = [
    ["Carne a la llanera", 40000],
    ["Mamona", 28000],
    ["Sobrebarriga asada", 27000],
    ["Costillas BBQ", 45000],
    ["Churrasco", 35000],
    ["Pechuga a la plancha", 20000],
    ["Hamburguesa artesanal", 18000],
    ["Perro caliente especial", 14000],
    ["Arepa con queso", 8000],
    ["Patacón con carne", 16000],
    ["Salchipapa mixta", 19000],
    ["Cerveza", 7000],
    ["Jugo natural", 6500],
    ["Jarra de limonada", 8000],
    ["Agua", 4000]
]

# ==========================================================
# MATRIZ DE PEDIDOS
# pedidos[mesa] = lista de productos
# ==========================================================

pedidos = [[] for _ in range(NUM_MESAS)]

# ==========================================================
# VARIABLES GLOBALES DE VENTAS
# ==========================================================

ventas_totales = 0
productos_vendidos = []

# ==========================================================
# FECHA ACTUAL
# ==========================================================

ahora = datetime.datetime.now()
fecha_actual = ahora.strftime("%d/%m/%Y")

# ==========================================================
# TRADUCCIÓN DE DÍAS
# ==========================================================

dias = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

# ==========================================================
# VALIDAR NÚMEROS
# ==========================================================

def pedir_numero(mensaje, minimo=None, maximo=None):

    while True:

        try:

            numero = int(input(mensaje))

            if minimo is not None and numero < minimo:
                print("❌ Número fuera de rango")
                continue

            if maximo is not None and numero > maximo:
                print("❌ Número fuera de rango")
                continue

            return numero

        except ValueError:
            print("❌ Debe ingresar un número válido")


# ==========================================================
# MOSTRAR CARTA
# ==========================================================

def mostrar_carta():

    print("\n========== 🍽️ CARTA 🍽️ ==========\n")

    for i, producto in enumerate(carta, start=1):

        print(
            f"{i}. {producto[0]:30} "
            f"$ {producto[1]:,}"
        )


# ==========================================================
# AGREGAR PRODUCTO
# ==========================================================

def agregar_producto():

    mesa = pedir_numero(
        "\nIngrese número de mesa (1-10): ",
        1,
        NUM_MESAS
    )

    while True:

        mostrar_carta()

        producto = pedir_numero(
            "\nIngrese número del producto: ",
            1,
            len(carta)
        )

        pedidos[mesa - 1].append(producto - 1)

        print("✅ Producto agregado correctamente")

        decision = input(
            "\n¿Desea agregar otro producto? (si/no): "
        ).lower().strip()

        if decision == "no":
            break

        elif decision != "si":
            print("❌ Opción inválida")


# ==========================================================
# VER PEDIDO
# ==========================================================

def ver_pedido():

    mesa = pedir_numero(
        "\nIngrese número de mesa (1-10): ",
        1,
        NUM_MESAS
    )

    mesa_pedidos = pedidos[mesa - 1]

    if len(mesa_pedidos) == 0:
        print("❌ La mesa no tiene pedidos")
        return

    print(f"\n📋 PEDIDO MESA {mesa}\n")

    contador = Counter(mesa_pedidos)

    subtotal = 0

    for idx, cantidad in contador.items():

        nombre = carta[idx][0]
        precio = carta[idx][1]

        total_producto = precio * cantidad

        subtotal += total_producto

        print(
            f"{cantidad}x {nombre:25} "
            f"$ {total_producto:,}"
        )

    print(f"\n💰 Subtotal: $ {subtotal:,}")


# ==========================================================
# ELIMINAR PRODUCTO
# ==========================================================

def eliminar_producto():

    mesa = pedir_numero(
        "\nIngrese número de mesa (1-10): ",
        1,
        NUM_MESAS
    )

    mesa_pedidos = pedidos[mesa - 1]

    if len(mesa_pedidos) == 0:
        print("❌ No hay pedidos en esta mesa")
        return

    while True:

        print(f"\n❌ PRODUCTOS MESA {mesa}\n")

        for i, idx in enumerate(mesa_pedidos, start=1):

            print(
                f"{i}. {carta[idx][0]} "
                f"$ {carta[idx][1]:,}"
            )

        eliminar = pedir_numero(
            "\nNúmero del producto a eliminar: ",
            1,
            len(mesa_pedidos)
        )

        eliminado = mesa_pedidos.pop(eliminar - 1)

        print(
            f"✅ {carta[eliminado][0]} eliminado correctamente"
        )

        if len(mesa_pedidos) == 0:
            print("📌 La mesa quedó sin pedidos")
            break

        decision = input(
            "\n¿Desea eliminar otro producto? (si/no): "
        ).lower().strip()

        if decision == "no":
            break

        elif decision != "si":
            print("❌ Opción inválida")


# ==========================================================
# GENERAR FACTURA
# ==========================================================

def generar_factura():

    global ventas_totales

    mesa = pedir_numero(
        "\nIngrese número de mesa (1-10): ",
        1,
        NUM_MESAS
    )

    mesa_pedidos = pedidos[mesa - 1]

    if len(mesa_pedidos) == 0:
        print("❌ La mesa no tiene pedidos")
        return

    dia_actual = dias[ahora.strftime("%A")]

    print("\n====================================")
    print("        🍽️ SABORES DEL LLANO")
    print("====================================")

    print(f"📅 Fecha: {fecha_actual}")
    print(f"🪑 Mesa: {mesa}")
    print(f"📌 Día: {dia_actual}")

    print("\n----------- FACTURA -----------")

    contador = Counter(mesa_pedidos)

    subtotal = 0

    for idx, cantidad in contador.items():

        nombre = carta[idx][0]
        precio = carta[idx][1]

        total_producto = precio * cantidad

        subtotal += total_producto

        print(
            f"{cantidad}x {nombre:25} "
            f"$ {total_producto:,}"
        )

        # Guardar productos vendidos
        for _ in range(cantidad):
            productos_vendidos.append(nombre)

    print("--------------------------------")

    print(f"💰 Subtotal: $ {subtotal:,}")

    descuento = 0

    if dia_actual in DIAS_DESCUENTO:

        descuento = subtotal * DESCUENTO

        print(f"🎁 Descuento 10%: $ {descuento:,.0f}")

    total = subtotal - descuento

    print(f"💵 TOTAL: $ {total:,.0f}")

    print("====================================")

    # Acumular ventas del día
    ventas_totales += total

    # Liberar mesa
    pedidos[mesa - 1].clear()

    print("\n✅ Mesa liberada correctamente")


# ==========================================================
# REPORTE DIARIO
# ==========================================================

def reporte_diario():

    print("\n========== 📊 REPORTE DIARIO ==========\n")

    print(f"💰 Recaudo total del día: $ {ventas_totales:,.0f}")

    if len(productos_vendidos) == 0:

        print("\n❌ Aún no hay ventas registradas")
        return

    contador = Counter(productos_vendidos)

    producto_mas_vendido = contador.most_common(1)

    nombre = producto_mas_vendido[0][0]
    cantidad = producto_mas_vendido[0][1]

    print(
        f"\n🏆 Producto más vendido:"
        f"\n{name} ({cantidad} vendidos)"
    )

    print("\n📋 TODOS LOS PRODUCTOS VENDIDOS:\n")

    for producto, cantidad in contador.items():

        print(f"{producto:30} {cantidad} vendidos")


# ==========================================================
# MENÚ PRINCIPAL
# ==========================================================

def menu():

    opcion = 0

    while opcion != 7:

        print("\n========== MENÚ PRINCIPAL ==========")

        print("""
1. 📋 Ver carta
2. ➕ Añadir producto
3. ❌ Eliminar producto
4. 👀 Ver pedido
5. 🧾 Generar factura
6. 📊 Reporte diario
7. 🚪 Salir
""")

        opcion = pedir_numero(
            "Seleccione una opción: ",
            1,
            7
        )

        if opcion == 1:
            mostrar_carta()

        elif opcion == 2:
            agregar_producto()

        elif opcion == 3:
            eliminar_producto()

        elif opcion == 4:
            ver_pedido()

        elif opcion == 5:
            generar_factura()

        elif opcion == 6:
            reporte_diario()

        elif opcion == 7:
            print("\n👋 Gracias por usar el sistema")


# ==========================================================
# INICIAR PROGRAMA
# ==========================================================

menu()