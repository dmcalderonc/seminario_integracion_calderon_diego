for flexion in range(1, 6):
    print("Goku hace la flexión", flexion)

for numero in range(1, 11):
    print("Multiplicacion", 5, "*", numero, "=", numero * 5)

for numero in range(1, 11, 3):
    print("Multiplicacion", 5, "*", numero, "=", numero * 5)

avengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitán América", "estado": "Activo"},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": "Activo"}
]

print("Lista de avengers")
for avenger in avengers:
    print(f"ID: {avenger['id']} | Nombre: {avenger['nombre']}")

nombres = ['Pedro', 'Pablo', 'Juan']
for nombre in nombres:
    print("Nombre actual", nombre)

guerreros_poder = {
    "Goku": 9500,
    "Gohan": 6000,
    "Vegueta": 6000,
    "Piccolo": 4500
}

for nombre, poder in guerreros_poder.items():
    if poder >= 9000:
        print(nombre, "Puede enfrentarse a Freezer")
    else:
        print(nombre, "necesita entrenar más")

print("\nCiclo for anidados")
guerreros = ["Goku", "Vegueta", "Gohan", "Piccolo"]
for guerrero in guerreros:
    print("Turno de:", guerrero)
    for ronda in range(1, 4):
        print("  Ronda:", ronda)

print("\nBreak y Continue")
for guerrero in guerreros:
    if guerrero == "Piccolo":
        print("Se detiene el torneo con break al llegar a Piccolo")
        break
    if guerrero == "Vegueta":
        print("Saltando a Vegueta con continue...")
        continue
    print("Procesando a guerrero:", guerrero)

for sector in range(1, 11):
    if sector == 3:
        print("Sector 3 : Zona destruida, omitirla para continuar")
        continue
    print("Sector", sector, ": Trunks explora")
    if sector == 7:
        print("Sector 7 : Trunks detiene la busqueda")
        break