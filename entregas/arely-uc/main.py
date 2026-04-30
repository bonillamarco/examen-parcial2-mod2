# INSTRUCCIONES PARA EL ALUMNO:
# 1. Completa la lógica de las funciones abajo definidas.
# 2. Asegúrate de que los parámetros y retornos sean correctos.
# 3. El programa debe ejecutarse sin errores al finalizar.
# 4. Complementa la documentación de las funciones, agregando los paramentros y retornos si aplica.

def calcular_promedio(lista_ventas):
    """
    Recibe una lista de números y devuelve el promedio.
    Fórmula: suma de elementos / cantidad de elementos.
    """
    # TODO: Implementar lógica aquí
    # Pista: Usa las funciones built-in sum() y len()

def evaluar_meta(total):
    """
    Si el total es mayor o igual a 1000, retorna "Meta Alcanzada".
    Si es menor, retorna "Meta No Alcanzada".
    """
    # TODO: Implementar estructura de control if/else aquí

def main():
    print("--- REPORTE DE VENTAS DIARIAS ---")
    
    # Datos de prueba (No modificar)
    datos = [200, 450, 100, 300, 50]
    
    # --- BLOQUE A REPARAR ---
    # El alumno debe calcular el total, el promedio y la meta.
    
    total = sum(datos)
    
    # Llamada a las funciones (quitar el 'None' y asignar la función correcta)
    promedio = None 
    resultado_meta = None
    
    # --- SALIDA DE DATOS ---
    print(f"Ventas totales: ${total}")
    print(f"Promedio de ventas: ${promedio}")
    print(f"Estado de la meta: {resultado_meta}")

if __name__ == "__main__":
    main()