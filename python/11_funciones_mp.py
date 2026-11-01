print("Funciones _mp")
print("Autor: Diego Calderón ")

def arrancar_motor():
    print("La motocicleta inyecta combustible")
    print("¡Motor encendido (Braap)!")

arrancar_motor()
arrancar_motor()
arrancar_motor()
arrancar_motor()

def iniciar_ruta(piloto):
    print(piloto, "inicia su recorrido en la ruta")

iniciar_ruta("Diego Calderón")
iniciar_ruta("Doménica")
iniciar_ruta("Mateo")
iniciar_ruta("Joel")

def calcular_distancia(velocidad, horas):
    distancia = velocidad * horas
    return distancia

resultado = calcular_distancia(80, 2)
print("La distancia recorrida por Diego Calderón es :", resultado, "km")

resultado = calcular_distancia(120, 5)
print("La distancia en pista de la moto es :", resultado, "km")

def activar_modo_pista(modelo, rpm):
    if rpm >= 9000:
        print(f"¡Modo pista activado con éxito para la {modelo}!")
    else:
        print(f"La {modelo} necesita aumentar sus revoluciones.")

activar_modo_pista("Yamaha MT-07", 5000)
activar_modo_pista("Yamaha MT-09", 10500)

modelo_moto: str = "Yamaha MT-09"
cilindraje: int = 890
peso_kg: float = 189.0
esta_activa: bool = True

def calcular_consumo(litros_por_hora: float, horas: int) -> float:
    return litros_por_hora * horas

consumo: float = calcular_consumo(4.5, 2)
print("Consumo de combustible calculado:", consumo, "litros")