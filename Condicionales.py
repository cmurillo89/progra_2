# Estructura condicional

# Usamos una sentencia IF para escribir código que se adapta a diferentes situaciones. Lo reconocemos por la palabra reservada IF

saludo = True

if saludo:
    print("Introducción a estructuras")
    print("Yo soy un bloque de código")

online = True
user = "Karen"
if online:
    print(user,"está en línea")

# Le sumamos al if la palabra ELSE

cargado = False
if cargado:
    print("Cargado")
else:
    print("Batería baja")

# UTILIZACION DE IF CON VARIAS CONDICIONALES O COMO LO LLAMAMOS UN IF ANIDADO

hour = 25
print(type(hour))

print(type(int(hour)))
if int(hour) < 12:
    print("Good morning")
elif int(hour) < 18:
    print("Good afternoon")
elif int(hour) <= 24:
    print("Good night")
else:
    print("Esta hora no existe")

# El uso de condicionales incluyentes y excluyentes (Y/O)

edad = 16
permitido = True
asegurado = False

if edad >= 18 and permitido or asegurado:
    print("Puede conducir")

