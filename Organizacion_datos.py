import random

# ARRAYS

tareas = ["LEER","LIMPIAR","COMER","PROGRAMAR"]
tareas.append("EJERCICIO")
tareas.insert(2,"TRABAJAR")
print(tareas)

# HAY UNA MANERA FACIL DE RECORRER EL BUCLE TODOS LOS ELEMENTOS DE LA LISTA USANDO UN BUCLE FOR

edades = [24,15,18,18,25,26,20,22,22,21]

filtrados = []
for edad in edades:
    if edades.count(edad) > 1:
        if edad not in filtrados:
            filtrados.append(edad)

print(filtrados)
        

print("El número máximo es:", max(edades))
print("El número mínimo es:", min(edades))
edades.sort()
print(edades[0])
print(sum(edades))
print(edades.count(22))




# Usamos la instruccion LEN() con el nombre de la lista entre par{entesis para obtener el número de elementosen una lista}

usuarios = ["cmurillo","kmonge","wjimenez","achavez"]
offline_user = ["agamboa","kgutierrez"]

num_usuarios = len(usuarios)

if num_usuarios > 0:
    for usuario in usuarios:
        print(usuario)
else:
    print("No hay nadie conectado")

print(usuarios + offline_user)

nombre = ""

separado = nombre.split()
print(separado)



aleatorio = [24,15,18,18,25,26,20,22,22,21]
print(random.choice(aleatorio))

# Trabajo en clase: Ordenar una lista de números de menor a mayor sin usar la función SORT()