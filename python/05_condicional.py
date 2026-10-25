print("Condicional if")
print("Condicional simple")
dinero=10
if dinero >= 5:
    print("Homero puede comprar rosquillas")

print("Programa finalizó")


print("Condicional if - else")
print("Condicional de dos caminos")
creditos = float(input("Cantidad de creditos disponibles: "))
precio_respuesta =float(input("Precio repuesto: "))

if (creditos>=precio_respuesta):
    print("Compra Autorizada")
else:
    print("Creditos insuficientes")
    print("Buscar solucion o trueque")


print("Condicional if - elif - else")
print("Condicional de tres caminos")
combustible = float(input("Combustible de la nave: "))

if (combustible>=75):
    print("Óptimo")
elif (combustible>=50):
    print("Suficiente")
elif (combustible>=20):
    print("Bajo")   
else:
    print("Critico")
    print("Localiza base más cercana") 


piloto =input("Nombre del piloto: ")
motor_funciona =input("El motor funciona SI/NO: ")
combustible = int(input("Combustible de la nave: "))


if (motor_funciona =="SI"):
    print("Compra Autorizada")
    if combustible >= 50:
        print("Combustible suficiente")
        print("Participacion autorizada")
    else:
        print("Debe recargar combustible")
else:
    print("No puede participar")
    print("El motor necesita reparacion")
