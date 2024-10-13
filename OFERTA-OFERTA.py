import os

# Función para guardar las tiendas en un archivo de texto
def guardar_tiendas(lista_tiendas):
    with open("tiendas_disponibles.txt", "w") as archivo:
        for tienda in lista_tiendas:
            archivo.write(f"{tienda}\n")

# Función para cargar las tiendas desde un archivo de texto
def cargar_tiendas():
    tiendas_predefinidas = ["Walmart", "Chedraui", "Soriana", "Coppel"]
    lista_tiendas = []

    if os.path.exists("tiendas_disponibles.txt"):
        with open("tiendas_disponibles.txt", "r") as archivo:
            lista_tiendas = [linea.strip() for linea in archivo]


    if not lista_tiendas:
        lista_tiendas = tiendas_predefinidas[:]
        guardar_tiendas(lista_tiendas)  # Guardar las tiendas predefinidas

    return lista_tiendas

# Función para elegir una tienda o agregar una nueva
def elegir_tienda(lista_tiendas):
    print("\n--- Tiendas Disponibles ---")
    for i, tienda in enumerate(lista_tiendas, 1):
        print(f"{i}. {tienda}")
    print(f"{len(lista_tiendas) + 1}. Agregar una nueva tienda")

    opcion = int(input("Elige una tienda por número o agrega una nueva: "))
    
    if opcion == len(lista_tiendas) + 1:  # Elige agregar una nueva tienda
        nueva_tienda = input("Ingresa el nombre de la nueva tienda: ")
        lista_tiendas.append(nueva_tienda)
        guardar_tiendas(lista_tiendas)  # Guardar la nueva tienda en el archivo
        return nueva_tienda
    elif 1 <= opcion <= len(lista_tiendas):  # Elige una tienda existente
        return lista_tiendas[opcion - 1]
    else:
        print("Opción no válida. Intentando de nuevo.")
        return elegir_tienda(lista_tiendas)

# Funciones de cálculo de las diferentes ofertas desde 3x2, 2x1, 2x1.5 y disntitos % del usuario
def oferta_3x2(cantidad, precio_unitario):
    grupo = cantidad // 3  
    productos_a_pagar = grupo * 2 + (cantidad % 3)  
    total = productos_a_pagar * precio_unitario
    ahorro = (cantidad - productos_a_pagar) * precio_unitario
    return total, ahorro

def calcular_oferta_2x1(cantidad, precio_unitario):
    total = 0
    ahorro = 0
    for i in range(0, cantidad, 2):
        if i + 1 < cantidad:  
            total += precio_unitario  
            ahorro += precio_unitario  
        else: 
            total += precio_unitario  
    return total, ahorro

def calcular_oferta_2x1_5(cantidad, precio_unitario):
    total = 0
    ahorro = 0
    for i in range(0, cantidad, 2):
        if i + 1 < cantidad:
            total += precio_unitario + (precio_unitario * 0.5)  
            ahorro += precio_unitario * 0.5  
        else:
            total += precio_unitario  
    return total, ahorro

def calcular_descuento_porcentaje(cantidad, precio_unitario, porcentaje_descuento):
    total = cantidad * precio_unitario
    ahorro = total * (porcentaje_descuento / 100)
    total_con_descuento = total - ahorro
    return total_con_descuento, ahorro

# Función de pruebas
def pruebas():
    print("\n--- INICIANDO PRUEBAS AUTOMÁTICAS ---")
    
    print("\nPrueba 1: Oferta 3x2 (Cantidad: 6, Precio unitario: 50)")
    total, ahorro = oferta_3x2(6, 50)
    print(f"Total esperado: 200, Total calculado: {total}")
    print(f"Ahorro esperado: 100, Ahorro calculado: {ahorro}")

    print("\nPrueba 2: Oferta 2x1 (Cantidad: 5, Precio unitario: 30)")
    total, ahorro = calcular_oferta_2x1(5, 30)
    print(f"Total esperado: 90, Total calculado: {total}")
    print(f"Ahorro esperado: 60, Ahorro calculado: {ahorro}")

    print("\nPrueba 3: Oferta 2x1.5 (Cantidad: 4, Precio unitario: 40)")
    total, ahorro = calcular_oferta_2x1_5(4, 40)
    print(f"Total esperado: 140, Total calculado: {total}")
    print(f"Ahorro esperado: 40, Ahorro calculado: {ahorro}")

    print("\nPrueba 4: Descuento por porcentaje (Cantidad: 10, Precio unitario: 25, Descuento: 20%)")
    total, ahorro = calcular_descuento_porcentaje(10, 25, 20)
    print(f"Total esperado: 200, Total calculado: {total}")
    print(f"Ahorro esperado: 50, Ahorro calculado: {ahorro}")


def main():
    lista_tiendas_disponibles = cargar_tiendas()  # Cargar las tiendas desde el archivo
    lista_tiendas = []  # Almacena las tiendas y los ahorros comparados

    while True:
        print("\n Bienvenido a Oferta Oferta ")
        print("1. Calcular ahorro")
        print("2. Comparar ahorros entre tiendas")
        print("3. Pruebas")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            tienda = elegir_tienda(lista_tiendas_disponibles)  
            tipo_oferta = input("Ingresa el tipo de oferta (3x2, 2x1, 2x1.5, porcentaje): ").lower()
            cantidad = int(input("Ingresa la cantidad de productos: "))
            precio_unitario = float(input("Ingresa el precio unitario del producto: "))

            if tipo_oferta == '3x2':
                total, ahorro = oferta_3x2(cantidad, precio_unitario)
            elif tipo_oferta == '2x1':
                total, ahorro = calcular_oferta_2x1(cantidad, precio_unitario)
            elif tipo_oferta == '2x1.5':
                total, ahorro = calcular_oferta_2x1_5(cantidad, precio_unitario)
            elif tipo_oferta == 'porcentaje':
                porcentaje_descuento = float(input("Ingresa el porcentaje de descuento: "))
                total, ahorro = calcular_descuento_porcentaje(cantidad, precio_unitario, porcentaje_descuento)
            else:
                print("Tipo de oferta no válido.")
                continue

            print(f"\nTotal a pagar: {total:.2f}")
            print(f"Ahorro obtenido en {tienda}: {ahorro:.2f}")
            lista_tiendas.append((tienda, ahorro))  

        elif opcion == '2':
            if not lista_tiendas:
                print("Es necesario ingresar una tienda ")
            else:
                print("\n Comparación de ahorros ")
                for tienda, ahorro in lista_tiendas:
                    print(f"Tienda: {tienda}, Ahorro: {ahorro:.2f}")

        elif opcion == '3':
            pruebas()  

        elif opcion == '4':
            print("VUELVE PRONTO, GRACIAS POR USAR OFERTA OFERTA...")
            break

        else:
            print(" ERROR--- Vuelve a intentarlo -_-")

main()

