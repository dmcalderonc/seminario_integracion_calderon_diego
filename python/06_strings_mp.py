"""
Manejo de Cadena de Caracteres
"""

modelo1 = "Yamaha MT-09"
print(f"Moto 1: {modelo1}")
print(f"Tipo de datos: {type(modelo1)}")

modelo2 = "Kawasaki Ninja"
print(f"Moto 2: {modelo2}")
print(f"Tipo de datos: {type(modelo2)}")

print("Funciones comunes de texto")
chasis_1 = "VIN-1002"
chasis_2 = "VIN-2005"
longitud_chasis_1 = len(chasis_1)
longitud_chasis_2 = len(chasis_2)
print("nombre chasis 1", chasis_1)
print("longitud chasis 1", longitud_chasis_1)
print("nombre chasis 2", chasis_2)
print("longitud chasis 2", longitud_chasis_2)

print("Convertir Mayusculas y minusculas")
detalle = "La concesionaria entrega la motocicleta Yamaha"
detalle_mayuscula = detalle.upper()
detalle_minusculas = detalle.lower()

print("Mensaje original: ", detalle)
print("Mensaje mayusculas: ", detalle_mayuscula)
print("Mensaje minusculas: ", detalle_minusculas)

print("Remplazo de substring")
detalle = "La moto se enviara a Guayaquil"
nuevo_detalle = detalle.replace("Guayaquil", "Quito")
print("Mensaje Original: ", detalle)
print("Mensaje Remplazado: ", nuevo_detalle)

marcas = "Yamaha, Kawasaki, Ducati"
print("marcas: ", marcas)
lista_marcas = marcas.split(",")
print(lista_marcas)
print("primer planeta: ", lista_marcas[0])

print("Extraer subcadenas")
detalle = "Gran potencia en pista asegurada siempre"
adjetivo = detalle[7:13]
verbo = detalle[17:25]
print("adjetivo es : ", adjetivo)
print("verbo es : ", verbo)

print("Comprobaciones utiles")
codigo = "MT09"
numero = "2026"
nombre = "Yamaha Motors"
identificador = "MOTO1"
print(codigo.isalnum())
print(numero.isdigit())
print(nombre.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())