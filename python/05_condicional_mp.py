print("Condicional if")
print("Condicional simple")
presupuesto = 10000
if presupuesto >= 5000:
    print("Cliente puede comprar la Yamaha MT-09")

print("Programa finalizó")


print("Condicional if - else")
print("Condicional de dos caminos")
credito_aprobado = float(input("Monto de crédito preaprobado: "))
precio_moto = float(input("Precio de la motocicleta: "))

if (credito_aprobado >= precio_moto):
    print("Venta Autorizada")
else:
    print("Crédito insuficiente")
    print("Buscar plan de financiamiento alternativo")


print("Condicional if - elif - else")
print("Condicional de tres caminos")
combustible = float(input("Nivel de combustible en tanque (%): "))

if (combustible >= 75):
    print("Óptimo")
elif (combustible >= 50):
    print("Suficiente")
elif (combustible >= 20):
    print("Bajo")
else:
    print("Crítico")
    print("Cargar combustible antes de la entrega")


cliente = input("Nombre del cliente: ")
motor_operativo = input("¿El motor supera la inspección mecánica? SI/NO: ")
combustible = int(input("Nivel de combustible (%): "))


if (motor_operativo == "SI"):
    print("Entrega Autorizada")
    if combustible >= 50:
        print("Combustible suficiente")
        print("Prueba de manejo autorizada")
    else:
        print("Debe recargar combustible")
else:
    print("No puede salir a prueba")
    print("La motocicleta necesita revisión técnica")
