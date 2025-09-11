import datetime

# IVA en Chile (19%)
IVA = 0.19

# Base de productos (puede crecer dinámicamente)
productos = {}

def registrar_producto():
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto (sin IVA): "))
    productos[codigo] = {"nombre": nombre, "precio": precio}
    print(f"✅ Producto '{nombre}' registrado.\n")

def mostrar_productos():
    print("\n📦 Productos registrados:")
    for codigo, datos in productos.items():
        print(f"{codigo} - {datos['nombre']} - ${datos['precio']:.0f}")
    print()

def nueva_venta():
    carrito = []
    while True:
        mostrar_productos()
        codigo = input("Ingrese código del producto (o ENTER para terminar): ")
        if codigo == "":
            break
        if codigo in productos:
            carrito.append(productos[codigo])
            print(f"🛒 Agregado: {productos[codigo]['nombre']}")
        else:
            print("❌ Producto no encontrado.")

    if not carrito:
        print("⚠ No se vendió nada.")
        return

    # Calcular totales
    subtotal = sum(item["precio"] for item in carrito)
    iva = subtotal * IVA
    total = subtotal + iva

    # Crear boleta
    fecha = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    boleta = []
    boleta.append("======== BOLETA ELECTRÓNICA ========")
    boleta.append(f"Fecha: {fecha}\n")
    for item in carrito:
        boleta.append(f"{item['nombre']}  ${item['precio']:.0f}")
    boleta.append("\n-----------------------------------")
    boleta.append(f"Subtotal: ${subtotal:.0f}")
    boleta.append(f"IVA (19%): ${iva:.0f}")
    boleta.append(f"TOTAL: ${total:.0f}")
    boleta.append("===================================\n")

    # Guardar boleta en archivo
    nombre_archivo = f"boleta_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("\n".join(boleta))

    print("\n".join(boleta))
    print(f"🧾 Boleta guardada en: {nombre_archivo}\n")

def menu():
    while True:
        print("=== SISTEMA DE PUNTO DE VENTA ===")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Nueva venta")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            nueva_venta()
        elif opcion == "4":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()