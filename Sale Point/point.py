import flet as ft
import datetime

# IVA en Chile (19%)
IVA = 0.19

# Base de productos (puede crecer dinámicamente)
productos = {}


def main(page: ft.Page):
    page.title = "💻 Punto de Venta" #Nombre de tienda/negocio
    page.theme_mode = "dark" 
    page.scroll = "auto"


    # Elementos de UI
    codigo_input = ft.TextField(label="Código del producto", width=200)
    nombre_input = ft.TextField(label="Nombre del producto", width=200)
    precio_input = ft.TextField(label="Precio sin IVA", width=200, keyboard_type="number")
    salida = ft.Text(value="📦 Productos registrados aparecerán aquí", selectable=True)
    carrito_view = ft.Column()

    # Función: registrar producto
    def registrar_producto(e):
        codigo = codigo_input.value.strip()
        nombre = nombre_input.value.strip()
        try:
            precio = float(precio_input.value)
        except:
            snack = ft.SnackBar(ft.Text("⚠ Ingrese un precio válido"), bgcolor="red")
            page.overlay.append(snack)
            snack.open = True
            page.update()
            return

        if codigo and nombre:
            productos[codigo] = {"nombre": nombre, "precio": precio}
            salida.value = mostrar_productos()
            codigo_input.value, nombre_input.value, precio_input.value = "", "", ""
            page.update()
        else:
            snack = ft.SnackBar(ft.Text("❌ Complete todos los campos"), bgcolor="red")
            page.overlay.append(snack)
            snack.open = True
            page.update()

    # Mostrar productos
    def mostrar_productos():
        lista = "Productos registrados:\n"
        for codigo, datos in productos.items():
            lista += f"{codigo} - {datos['nombre']} - ${datos['precio']:.0f}\n"
        return lista if productos else "⚠ No hay productos registrados ⚠"

    # Nueva venta: agregar producto al carrito
    def agregar_al_carrito(codigo):
        if codigo in productos:
            item = productos[codigo]
            carrito_view.controls.append(
                ft.Text(f"{item['nombre']} - ${item['precio']:.0f}", data=codigo)
            )
            page.update()
        else:
            snack = ft.SnackBar(ft.Text("❌ Producto no encontrado"), bgcolor="red")
            page.overlay.append(snack)
            snack.open = True
            page.update()

    # Generar boleta
    def generar_boleta(e):
        if not carrito_view.controls:
            snack = ft.SnackBar(ft.Text("⚠ Carrito vacío"), bgcolor="orange")
            page.overlay.append(snack)
            snack.open = True
            page.update()
            return

        # Calcular totales usando el código (data)
        subtotal = sum(productos[c.data]["precio"] for c in carrito_view.controls if isinstance(c, ft.Text))
        iva = subtotal * IVA
        total = subtotal + iva

        fecha = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        boleta = [
            "======== BOLETA ELECTRÓNICA ========",
            f"Fecha: {fecha}\n"
        ]

        for item in carrito_view.controls:
            boleta.append(item.value)

        boleta += [
            "\n-----------------------------------",
            f"Subtotal: ${subtotal:.0f}",
            f"IVA (19%): ${iva:.0f}",
            f"TOTAL: ${total:.0f}",
            "===================================\n"
        ]

        # Guardar en archivo
        nombre_archivo = f"boleta_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("\n".join(boleta))

        # Mostrar en un diálogo
        dlg = ft.AlertDialog(
            title=ft.Text("🧾 Boleta generada"),
            content=ft.Text("\n".join(boleta)),
            actions=[ft.TextButton("OK", on_click=lambda e: page.dialog.close())]
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    # UI principal
    page.add(
        ft.Column(
        [
        ft.Text("=== 🛍️ Sistema de Punto de Venta ===", size=20, weight="bold"),
        ft.Row([codigo_input, nombre_input, precio_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.ElevatedButton("Registrar producto", on_click=registrar_producto),
        salida,
        ft.Divider(),
        ft.Text("🛒 Carrito de compras:", size=20, weight="bold"),
            carrito_view,
        ft.Row([
            ft.TextField(
                label="Código para agregar al carrito",
                width=280,
                on_submit=lambda e: agregar_al_carrito(e.control.value)
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.ElevatedButton("Generar Boleta", on_click=generar_boleta),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)