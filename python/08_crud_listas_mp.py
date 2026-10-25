print("CRUD DE LISTAS EN PYTHON - INVENTARIO DE MOTOCICLETAS")

motos = [
    {"id": 1, "modelo": "MT-09", "marca": "Yamaha", "estado": "Disponible"},
    {"id": 2, "modelo": "Ninja ZX-6R", "marca": "Kawasaki", "estado": "Disponible"},
    {"id": 3, "modelo": "CBR600RR", "marca": "Honda", "estado": "Disponible"}
]

id_publico = 4

def create():
    global id_publico

    print("Registrar Motocicleta")

    modelo = input("Modelo: ")
    marca = input("Marca: ")
    estado = input("Estado (Disponible, Reservada, Vendida, Taller): ")

    nueva_moto = {
        "id": id_publico,
        "modelo": modelo,
        "marca": marca,
        "estado": estado
    }

    motos.append(nueva_moto)
    id_publico += 1

def read():
    print("Inventario de motocicletas")
    for moto in motos:
        print(f"{moto['id']} - modelo : {moto['modelo']} ({moto['marca']}) - {moto['estado']}")

def update():
    print("Actualizar motocicleta")
    id_update = int(input("id a modificar: "))
    for moto in motos:
        if moto["id"] == id_update:
            moto["modelo"] = input("Nuevo modelo: ")
            moto["marca"] = input("Nueva marca: ")
            moto["estado"] = input("Nuevo estado: ")
            print("Actualizado")
            break

def delete():
    print("Eliminar motocicleta")
    id_delete = int(input("id a eliminar: "))
    for moto in motos:
        if moto["id"] == id_delete:
            motos.remove(moto)
            print("Motocicleta eliminada")
            break

def menu():
    while True:
        print("\n1. Registrar")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")

        option = input("Seleccione 1 al 5: ")

        if option == "1":
            create()

        elif option == "2":
            read()

        elif option == "3":
            update()

        elif option == "4":
            delete()

        elif option == "5":
            print("Cerrando sistema")
            break

        else:
            print("intente nueva opcion")


if __name__ == "__main__":
    menu()
