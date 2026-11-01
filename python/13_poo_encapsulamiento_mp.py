class Motocicleta:
    modelo: str
    __cilindraje: int

    def __init__(self, modelo: str, cilindraje: int):
        self.modelo = modelo
        self.__cilindraje = cilindraje 

    def mostrar_info(self):
        print(f"Modelo: {self.modelo} | Cilindraje: {self.__cilindraje}cc")

    def get_cilindraje(self) -> int:
        return self.__cilindraje


yamaha_mt09 = Motocicleta("Yamaha MT-09", 890)
yamaha_mt07 = Motocicleta("Yamaha MT-07", 689)
ducati_monster = Motocicleta("Ducati Monster", 937)
honda_cb650 = Motocicleta("Honda CB650R", 649)


yamaha_mt09.mostrar_info()
yamaha_mt07.mostrar_info()
ducati_monster.mostrar_info()
honda_cb650.mostrar_info()

print(yamaha_mt09.modelo)
print(yamaha_mt07.modelo)
print(ducati_monster.modelo)
print(honda_cb650.modelo)

# Nota: Añadí los paréntesis () al final que faltaban en tu código original para que el método se ejecute correctamente
print(yamaha_mt07.get_cilindraje())