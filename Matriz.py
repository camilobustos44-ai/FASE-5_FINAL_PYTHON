def calcular_pedido(stock_actual, stock_minimo):
    """
    Módulo para determinar la cantidad exacta a pedir de un artículo.
    """
    # Regla de negocio: Si el Stock Actual es menor al Stock Mínimo
    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
        return cantidad_a_pedir
    # Regla de negocio: Si el Stock Actual es suficiente (mayor o igual)
    else:
        return 0

def solicitar_entero(mensaje):
    """
    Función que valida que el usuario ingrese obligatoriamente un número entero válido.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("-> Error: No se permiten valores negativos. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("-> Error: Entrada inválida. Por favor, ingrese únicamente números enteros.")

def auditar_inventario():
    """
    Función principal que maneja el registro dinámico, la matriz y la impresión de los datos.
    """
    inventario = []
    
    print("=" * 60)
    print("   SISTEMA DE AUDITORÍA DE INVENTARIO ELECTRÓNICO   ")
    print("=" * 60)
    
    # Solicitar cantidad de artículos con validación
    cantidad = solicitar_entero("¿Cuántos artículos desea registrar en el sistema?: ")
    
    # Llenado dinámico de la matriz
    for i in range(cantidad):
        print(f"\n--- Registrando Artículo {i+1} de {cantidad} ---")
        codigo = input("Ingrese el código del artículo: ")
        nombre = input("Ingrese el nombre del artículo: ")
        # Uso de la función de validación para asegurar que no ingresen letras
        stock_actual = solicitar_entero(f"Ingrese el stock actual de '{nombre}': ")
        stock_minimo = solicitar_entero(f"Ingrese el stock mínimo requerido de '{nombre}': ")
        
        # Almacenando en la matriz bidimensional
        inventario.append([codigo, nombre, stock_actual, stock_minimo])

    print("\n" + "=" * 60)
    print("                REPORTE DE AUDITORÍA                ")
    print("=" * 60)
    print(f"{'Nombre del Artículo':<25} | {'Cantidad a Pedir'}")
    print("-" * 60)

    # Recorrido de la matriz para generar el reporte
    for articulo in inventario:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        # Llamado al módulo lógico
        pedido = calcular_pedido(stock_actual, stock_minimo)

        # Imprimir resultados
        if pedido > 0:
            print(f"{nombre:<25} | Pedir: {pedido} unidades")
        else:
            print(f"{nombre:<25} | No requiere pedido (Unidades actuales: {stock_actual}")

# Ejecución del programa
if __name__ == "__main__":
    auditar_inventario()
