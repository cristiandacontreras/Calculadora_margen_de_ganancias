import flet as ft

def main(page: ft.Page):
    # Configuraciones de página seguras a prueba de versiones
    page.title = "Calculadora de Margen"
    page.theme_mode = "dark"
    
    # Manejo de tamaño de ventana actualizado (Flet 1.0+)
    page.window.width = 500
    page.window.height = 800
    page.padding = 30
    page.scroll = "auto" 

    titulo = ft.Text("Calculadora de Rentabilidad", size=24, weight="bold")

    # Usamos strings en keyboard_type para evitar errores de Enum
    costo_shein = ft.TextField(label="Costo Prenda Shein ($)", value="29000", keyboard_type="number")
    envio_shein = ft.TextField(label="Envío Shein ($)", value="40000", keyboard_type="number")
    garantia = ft.TextField(label="Garantía de envío ($)", value="1592", keyboard_type="number")
    impuestos = ft.TextField(label="Impuestos Tarjeta/Aduana (%)", value="50", keyboard_type="number")
    
    envio_ml = ft.TextField(label="Tu parte del Envío ML ($)", value="7470", keyboard_type="number")
    comision_ml = ft.TextField(label="Comisión Mercado Libre (%)", value="15.5", keyboard_type="number")
    margen = ft.TextField(label="Margen de Ganancia Esperado (%)", value="30", keyboard_type="number")

    # Colores Hexadecimales puros para evitar el __getattr__
    resultado_precio = ft.Text("Precio de Venta Ideal: $0.00", size=20, weight="bold", color="#66bb6a") # Verde
    resultado_ganancia = ft.Text("Tu Ganancia Limpia: $0.00", size=18, weight="bold", color="#42a5f5") # Azul
    resultado_desglose = ft.Text("", size=14, color="#cccccc") # Gris

    def calcular_rentabilidad(e):
        try:
            c_shein = float(costo_shein.value)
            e_shein = float(envio_shein.value)
            garantia_val = float(garantia.value)
            impuestos_val = float(impuestos.value) / 100
            
            e_ml = float(envio_ml.value)
            com_ml = float(comision_ml.value) / 100
            margen_val = float(margen.value) / 100

            costo_base_shein = c_shein + e_shein + garantia_val
            costo_total_shein = costo_base_shein * (1 + impuestos_val)
            costo_fijo_total = costo_total_shein + e_ml

            divisor = 1 - com_ml - margen_val

            if divisor <= 0:
                resultado_precio.value = "Error: Margen + Comisión >= 100%"
                resultado_precio.color = "#ef5350" # Rojo
                resultado_ganancia.value = ""
                resultado_desglose.value = "Revisá los porcentajes ingresados."
                page.update()
                return

            precio_venta = costo_fijo_total / divisor
            ganancia_neta = precio_venta * margen_val
            comision_total_ml = precio_venta * com_ml

            resultado_precio.value = f"Precio de Venta Ideal: ${precio_venta:,.2f}"
            resultado_precio.color = "#66bb6a"
            resultado_ganancia.value = f"Tu Ganancia Limpia: ${ganancia_neta:,.2f}"
            resultado_desglose.value = (
                f"--- Desglose ---\n"
                f"Costo Total Shein (con {impuestos.value}% imp): ${costo_total_shein:,.2f}\n"
                f"Costo Fijo (Shein + Envío ML): ${costo_fijo_total:,.2f}\n"
                f"Lo que se cobra Mercado Libre: ${comision_total_ml:,.2f}"
            )
            page.update()

        except ValueError:
            resultado_precio.value = "Por favor, ingresá solo números válidos."
            resultado_precio.color = "#ef5350" # Rojo
            resultado_ganancia.value = ""
            resultado_desglose.value = ""
            page.update()

    # Botón seguro sin el error de text ni de ButtonStyle
    btn_calcular = ft.ElevatedButton(
        content=ft.Text("Calcular Precio de Venta", color="white", weight="bold"),
        on_click=calcular_rentabilidad,
        bgcolor="#1976d2" # Azul
    )

    tarjeta_resultados = ft.Container(
        content=ft.Column([resultado_precio, resultado_ganancia, resultado_desglose]),
        bgcolor="#2c2c2c", # Gris oscuro seguro
        padding=20,
        border_radius=10,
    )

    page.add(
        titulo,
        ft.Divider(),
        ft.Text("Costos de Shein", weight="bold", color="#90caf9"),
        costo_shein, envio_shein, garantia, impuestos,
        
        ft.Divider(),
        ft.Text("Costos y Variables de Venta (Mercado Libre)", weight="bold", color="#90caf9"),
        envio_ml, comision_ml, margen,
        
        ft.Container(height=10),
        ft.Row([btn_calcular], alignment="center"),
        ft.Container(height=10),
        
        tarjeta_resultados
    )#aa

ft.app(target=main)