# INSTRUCCIONES PARA EL ALUMNO:
# 1. Completa la lógica de las funciones abajo definidas.
# 2. Asegúrate de que los parámetros y retornos sean correctos.
# 3. El programa debe ejecutarse sin errores al finalizar.
# 4. Complementa la documentación de las funciones, agregando los parámetros y retornos si aplica.

def calcular_promedio(lista_ventas):
    """
    Calcula el promedio de una lista de ventas.

    Parámetros:
    lista_ventas (list): Lista de números (ventas).

    Retorna:
    float: Promedio de las ventas. Si la lista está vacía, retorna 0.
    """
    suma = sum(lista_ventas)
    cantidad = len(lista_ventas)
    
    if cantidad == 0:
        return 0
    
    return suma / cantidad


def evaluar_meta(total):
    """
    Evalúa si se alcanzó la meta de ventas.

    Parámetros:
    total (int o float): Total de ventas.

    Retorna:
    str: "Meta alcanzada" si el total es mayor o igual a 1000,
         de lo contrario "Meta no alcanzada".
    """
    if total >= 1000:
        return "Meta alcanzada"
    else:
        return "Meta no alcanzada"


def main():
    print("--- REPORTE DE VENTAS DIARIAS ---")
    
    # Datos de prueba (No modificar)
    datos = [200, 450, 100, 300, 50]
    
    # --- BLOQUE A REPARAR ---
    
    total = sum(datos)
    
    # Llamada a las funciones
    promedio = calcular_promedio(datos)
    resultado_meta = evaluar_meta(total)
    
    # --- SALIDA DE DATOS ---
    print(f"Ventas totales: ${total}")
    print(f"Promedio de ventas: ${promedio}")
    print(f"Estado de la meta: {resultado_meta}")


if __name__ == "__main__":
    main()