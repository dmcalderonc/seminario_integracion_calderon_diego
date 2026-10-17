print("Incluir Datos con Input")
nombre = input("¿Cuál es tu nombre? ")
print("¡Hola", nombre, "!")
print("Bienvenido a la Concesionaria de Motos")
print("Hasta pronto " + nombre)

cantidad_cascos = int(input("¿Cuántos cascos adicionales deseas comprar? "))
total_accesorios = cantidad_cascos + 2  # Se suman 2 pares de guantes que vienen de regalo
print("Accesorios totales a entregar: ", total_accesorios)

print("\n CONVERSIONES ")
print("==== CONCESIONARIA MOTOS CALDE ====")
nombre_cliente = input("Nombre del cliente: ")
precio = float(input("Precio de la motocicleta: "))
cantidad = int(input("Cantidad a comprar: "))
total = cantidad * precio

print("Total a pagar: ", total)
print("Total a pagar (round): ", round(total, 2))
print(f"Total a pagar (f): ${total:.2f}")