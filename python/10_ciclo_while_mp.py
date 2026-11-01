rpm = 2000

while rpm < 10000:
    print("La Yamaha MT-09 está acelerando...")
    rpm += 2000
print("¡La motocicleta alcanzó su máxima potencia!")

# Reutilizamos el valor de 10000 para la autonomía
autonomia = rpm 

while autonomia > 0:
    print("A la motocicleta le quedan", autonomia, "km de autonomía")
    autonomia -= 500

print("La motocicleta se quedó sin combustible")

print("\nContinue y break")
dia = 0
while dia < 10:
    dia += 1
    if dia == 4:
        print("Día 4: Moto en el taller para revisión rápida (continue)")
        continue

    print("Día", dia, ": Avanzando en la ruta de viaje")

    if dia == 8:
        print("Día 8: Llegada al destino final de la ruta (break)")
        break