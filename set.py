#set es una coleccion sin orden, y sin indice y no tienen elementos epetidos
# y los elementos no se pueden modificar, pero si nuevos o eliminar

planetas = {"Marte","Júpiter","Venus"}
print(planetas)
#largo
print(len(planetas))
#revisar si un elemento esta presente
print("Marte" in planetas)
#agregar
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra")# no se puede agregar elementos duplicados
print(planetas)
#eliminar con remove posiblemente arroja exepción
planetas.remove("Tierra")
print(planetas)
#eliminar con discar no arroja exepción
planetas.discard("Júpiter")
#limpiar el set
planetas.clear()
print(planetas)
#eliminar el set
del planetas
print(planetas)