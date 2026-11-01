class Motocicleta:
    modelo: str
    marca: str
    def __init__(self, modelo: str, marca: str):
        self.modelo = modelo
        self.marca = marca

    def mostrar_info(self):
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")

yamaha_mt09 = Motocicleta("MT-09", "Yamaha")
yamaha_mt07 = Motocicleta("MT-07", "Yamaha")
ducati_monster = Motocicleta("Monster", "Ducati")
honda_cb650 = Motocicleta("CB650R", "Honda")

yamaha_mt09.mostrar_info()
yamaha_mt07.mostrar_info()
ducati_monster.mostrar_info()
honda_cb650.mostrar_info()