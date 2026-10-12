print(" OPERADORES ")
print("Operadores Aritmeticos")
print(" + Suma: ", 5, "+" , 3, "=" , 5+3)
print(" - Resta: ", 5, "-" , 3, "=" , 5-3)
print(" * Multiplicación: ", 5, "*" , 3, "=" , 5*3)
print(" / Division: ", 5, "/" , 3, "=" , 5/3)
print(" // Division entera: ", 5, "//" , 3, "=" , 5//3)
print(" % Residuo: ", 5, "%" , 3, "=" , 5%3)
print(" ** Potencia: ", 5, "**" , 3, "=" , 5**3)



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


print("OPERADORES DE COMPARACION")
print(" == igual a: ", 5, "==" , 5, "=" , 5==5)
print(" == igual a: ", 5, "==" , 4, "=" , 5==4)
print(" != igual a: ", 5, "!=" , 5, "=" , 5!=5)
print(" != igual a: ", 5, "!=" , 4, "=" , 5!=4)
print(" > mayor que: ", 10, ">" , 18, "=" , 10>18)
print(" > mayor que: ", 18, ">" , 10, "=" , 18>10)
print(" < menor que: ", 10, "<" , 18, "=" , 10<18)
print(" < menor que: ", 18, "<" , 10, "=" , 18<10)

print(" >= mayor que o igual: ", 10, ">=" , 18, "=" , 10>=18)
print(" >= mayor que o igual: ", 18, ">=" , 10, "=" , 18>=10)
print(" <= menor que o igual: ", 10, "<=" , 18, "=" , 10<=18)
print(" <= menor que o igual: ", 18, "<=" , 10, "=" , 18<=10)



print("OPERADORES LOGICOS")
print("Operador and: (5==5)and (4>3)", (5==5)and(4>3))
print("Operador and: (5==5)and (4>8)", (5==5)and(4>8))
print("Operador and: (5==5)or (4>3)", (5==5)or(4>8))
print("Operador and: (5==5)or (4>3)", (5==6)or(4>8))
print("Operador not: not (5==5)", not(5==5))
print("Operador not: not (5==5)", not(5==6))

print("Operador not : not (5==5)", not (5==5))

tiene_dinero = True
tienda_abierta = True

puede_comprar = tiene_dinero and tienda_abierta
print("¿Puede comprar?", puede_comprar)

es_cliente_vip = True
tiene_dinero = False
acceso_credito = es_cliente_vip or tiene_dinero
print("¿Crédito aprobado?", acceso_credito)
