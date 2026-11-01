poder = 2000

while poder < 10000:
    print("Vegueta esta entrenando")
    poder += 2000
print("!Vegueta alcanzo su objetivo")

while poder >0:
    print("Majin Boo tiene", poder,' de poder')
    poder -= 500

print("Majin Boo tiene se quedo sin energia")

print("Continue y break")
dia = 0
while dia < 10:
    dia += 1
    if dia == 4:
        print("Día 4: Gohan estudia (continue)")
        continue

    print("Día", dia, ": Gohan entrena")

    if dia == 8:
        print("Día 8: Fin del entrenamiento (break)")
        break


