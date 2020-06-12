# un diccionario esta compuesto de llaves, valor(key,value)
diccionario = {
    "IDE":"Integrated Development Enviroment",
    "OOP":"Object Oriented Programming",
    "DBMS":"Database Managment System"
}

print(diccionario)
#largo
print(len(diccionario))
#acceder a un elemento
print(diccionario["IDE"])
#otra forma, mismo resultado
print(diccionario.get("IDE"))
#modificando valores
diccionario["IDE"]="Integrated Development enviroment"
print(diccionario)
#iterar
for termino in diccionario:
    print(termino)
    
for termino in diccionario:
    print(diccionario[termino])
    
for valor in diccionario.values():
    print(valor)  
    
#comprobar si existe un elemento
print("IDE" in diccionario)  
#agregar nuevos elementos
diccionario["PK"]="Primary key" 
print(diccionario) 
#remover elementos
diccionario.pop("DBMS")
print(diccionario) 
#limpiar
diccionario.clear()
print(diccionario) 
#eliminar por completo
del diccionario
print(diccionario)