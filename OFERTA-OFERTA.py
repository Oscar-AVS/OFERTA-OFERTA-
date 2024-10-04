def oferta_3x2(cantidad, precio_unitario):
    grupo = cantidad // 3 
    productos_a_pagar = grupo * 2 + (cantidad % 3)  
    total = productos_a_pagar * precio_unitario
    ahorro = (cantidad - productos_a_pagar) * precio_unitario
    return total, ahorro
""" Esta función permite calcular el total a pagar así como el ahorro en una oferta tipo 3x2. En donde cada grupo de 3 solamente se pagan 2 productos. Esto se realiza dividiendo la cantidad de productos en grupos de 3 y sumando alguno otro que no logre agruparse."""
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
“””Esta función calcula el total y el ahorro para la oferta de 2x1 . Por cada 2 productos, uno se paga. En esta función se agrupan en pares la cantidad de productos y alguno que sea impar se paga sin el descuento. “”” 
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

def main():
    while True:
        print("1. Calcular ahorro")
        print("2. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            tipo_oferta = input("Ingresa el tipo de oferta: \n 3x2, 2x1 o 2x1.5 \n").lower()
            cantidad = int(input("Ingresa la cantidad de productos: "))
            precio_unitario = float(input("Ingresa el precio unitario del producto: "))

            if tipo_oferta == '3x2':
                total, ahorro = oferta_3x2(cantidad, precio_unitario)
            elif tipo_oferta == '2x1':
                total, ahorro = calcular_oferta_2x1(cantidad, precio_unitario)
            elif tipo_oferta == '2x1.5':
                total, ahorro = calcular_oferta_2x1_5(cantidad, precio_unitario)
            
            print(f"Total a pagar: {total:.2f}")
            print(f"Ahorro obtenido: {ahorro:.2f}")
        
        elif opcion == '2':
            print("VUELVE PRONTO, GRACIAS POR USAR OFERTA OFERTA...")
            break

main()

