# Variables y tipos de datos
# Los tipos de variables son Integer, String, Float, Boolean

nombre = "Nayarith"
apellido = "Quesada"
apellido2 = "Chacon"
edad = 22
nombre_completo = nombre + " " + apellido + " " + apellido2 + " " + str(edad)
peso = 65
casado = True
soltero = not True
true = False

print(nombre_completo.upper())
print(type(nombre_completo))
print("Nombre: ", nombre,"tiene", edad, "años y pesa:", peso)

# ¿cómo comparamos los valores dentro de las variables? por medio del operador de igualdad ==
# Cómo verificar si el PIN ingresado por un usuario coincide su PIN guardado

pin_almacenado = 5448
pin_digitado = 5440

print(pin_almacenado == pin_digitado)
print(10 == 20)

print("5" + "3")
print(25 == 30)
print(12 + 6)

# Desigualdad

print(25 == 30)
print(25 != 30)

# Comparaciones 

print(25 > 25)
print(25 >= 25)

