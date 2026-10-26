class Guerrero:
    nombre: str
    __poder: int

    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self.__poder = poder 

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} | Poder: {self.__poder}")

    def get_poder(self) -> int:
        return self.__poder


goku = Guerrero("Goku", 9000)
vegueta = Guerrero("Vegueta", 6000)
piccolo = Guerrero("Piccolo", 10000)
diego = Guerrero("Diego", 5000)


goku.mostrar_info()
vegueta.mostrar_info()
piccolo.mostrar_info()
diego.mostrar_info()

print(goku.nombre)
print(vegueta.nombre)
print(piccolo.nombre)
print(diego.nombre)
print(vegueta.get_poder)