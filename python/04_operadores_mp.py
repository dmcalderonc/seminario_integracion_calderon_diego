print(" OPERADORES EN EL INVENTARIO DE MOTOS ")
print("Operadores Aritméticos")
print(" + Suma (Nuevas motos al inventario): ", 5, "+" , 3, "=" , 5+3)
print(" - Resta (Motos vendidas hoy): ", 5, "-" , 3, "=" , 5-3)
print(" * Multiplicación (Costo por 3 unidades): ", 5, "*" , 3, "=" , 5*3)
print(" / División (Mitad del lote): ", 5, "/" , 3, "=" , 5/3)
print(" // División entera (Motos completas por camión): ", 5, "//" , 3, "=" , 5//3)
print(" % Residuo (Motos sobrantes sin asignar): ", 5, "%" , 3, "=" , 5%3)
print(" ** Potencia (Cálculo de depreciación al cubo): ", 5, "**" , 3, "=" , 5**3)


print("\nTabla de importación (Cajas de 5 motos)")
print(" * Multiplicación: ", 5, "*" , 1, "=" , 5*1)
print(" * Multiplicación: ", 5, "*" , 2, "=" , 5*2)
print(" * Multiplicación: ", 5, "*" , 3, "=" , 5*3)
print(" * Multiplicación: ", 5, "*" , 4, "=" , 5*4)
print(" * Multiplicación: ", 5, "*" , 5, "=" , 5*5)
print(" * Multiplicación: ", 5, "*" , 6, "=" , 5*6)
print(" * Multiplicación: ", 5, "*" , 7, "=" , 5*7)
print(" * Multiplicación: ", 5, "*" , 8, "=" , 5*8)
print(" * Multiplicación: ", 5, "*" , 9, "=" , 5*9)
print(" * Multiplicación: ", 5, "*" , 10, "=" , 5*10)


print("\nOPERADORES DE COMPARACIÓN (Validando precios y stock)")
print(" == igual a (Mismo precio): ", 5, "==" , 5, "=" , 5==5)
print(" == igual a (Diferente precio): ", 5, "==" , 4, "=" , 5==4)
print(" != distinto a (Modelos diferentes): ", 5, "!=" , 5, "=" , 5!=5)
print(" != distinto a (Modelos diferentes): ", 5, "!=" , 4, "=" , 5!=4)
print(" > mayor que (Stock superior): ", 10, ">" , 18, "=" , 10>18)
print(" > mayor que (Stock superior): ", 18, ">" , 10, "=" , 18>10)
print(" < menor que (Falta de stock): ", 10, "<" , 18, "=" , 10<18)
print(" < menor que (Falta de stock): ", 18, "<" , 10, "=" , 18<10)

print(" >= mayor que o igual (Objetivo de ventas): ", 10, ">=" , 18, "=" , 10>=18)
print(" >= mayor que o igual (Objetivo de ventas): ", 18, ">=" , 10, "=" , 18>=10)
print(" <= menor que o igual (Límite de crédito): ", 10, "<=" , 18, "=" , 10<=18)
print(" <= menor que o igual (Límite de crédito): ", 18, "<=" , 10, "=" , 18<=10)


print("\nOPERADORES LÓGICOS (Aprobaciones en concesionaria)")
print("Operador and: (5==5) and (4>3)", (5==5) and (4>3))
print("Operador and: (5==5) and (4>8)", (5==5) and (4>8))
print("Operador or: (5==5) or (4>8)", (5==5) or (4>8))
print("Operador or: (5==6) or (4>8)", (5==6) or (4>8))
print("Operador not: not (5==5)", not(5==5))
print("Operador not: not (5==6)", not(5==6))

print("Operador not : not (5==5)", not (5==5))

tiene_dinero_entrada = True
concesionaria_abierta = True

puede_comprar_moto = tiene_dinero_entrada and concesionaria_abierta
print("¿El cliente puede comprar la moto hoy?", puede_comprar_moto)

es_cliente_vip = True
tiene_dinero_total = False
acceso_credito_directo = es_cliente_vip or tiene_dinero_total
print("¿Crédito para la moto aprobado?", acceso_credito_directo)