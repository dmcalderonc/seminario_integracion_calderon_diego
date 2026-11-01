print("Funciones ")
print("Autor: Diego Calderón ")

def kamehameha():
    print("Goku concentra su energia")
    print("!kamehameha")


kamehameha()
kamehameha()
kamehameha()
kamehameha()

def atacar(guerrero):
    print(guerrero, "realiza un ataque")

atacar("Goku")
atacar("Vegueta")
atacar("Piccolo")
atacar("Diego Calderon")

def calcular_poder(poder, ataques):
    danio = poder * ataques
    return danio

resultado = calcular_poder(4, 26)
print("El poder de Diego Calderon es :", resultado)

resultado = calcular_poder(4, 5000)
print("El poder de goku es :", resultado)


def transformar_sayajin(nombre, poder):
    if poder >= 9000:
        print(f"¡Transformación a Super Sayajin exitosa para {nombre}!")
    else:
        print(f"{nombre} necesita aumentar su poder.")


transformar_sayajin("Diego Calderon", 5000)
transformar_sayajin("Gohan", 15000)


nombre_personaje: str = "Goku"
edad: int = 33
altura: float = 1.74
es_activo: bool = True

def multiplicador_poder(entrenamiento: float, edad: int)-> float:
    return entrenamiento*edad

poder: float = multiplicador_poder(15.5,2)
print("Poder calculado", poder)

