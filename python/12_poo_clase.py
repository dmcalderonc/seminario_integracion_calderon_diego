class Guerrero:
    nombre: str
    raza: str
    def __init__(self, nombre: str, raza: str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")


goku = Guerrero("Goku", "Sayajin")
vegueta = Guerrero("Vegueta", "Sayajin")
piccolo = Guerrero("Picoolo", "Namekiano")
diego = Guerrero("Diego", "Humano")

goku.mostrar_info()
vegueta.mostrar_info()
piccolo.mostrar_info()
diego.mostrar_info()