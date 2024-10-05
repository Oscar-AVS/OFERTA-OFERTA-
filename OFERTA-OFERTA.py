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
def main():
    lista_tiendas = []  
    while True:
        print("\n Bienvenido a Oferta Oferta ")
        print("1. Calcular ahorro")
        print("2. Comparar ahorros entre tiendas")
        print("3. Pruebas")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            tienda = input("Ingresa el nombre de la tienda: ")  
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

      

        elif opcion == '4':
            print("VUELVE PRONTO, GRACIAS POR USAR OFERTA OFERTA...")
            break

        else:
            print(" ERROR--- Vuelve a intentarlo -_-")

main()

