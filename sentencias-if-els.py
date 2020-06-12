#condicion = 10
condicion = True
print("Condicion verdadera") if condicion else print("condicion falsa")



if condicion == True:
    print("La condicion es verdadera")
elif condicion == False:  
     print("La condicion es falsa")    
else:
    print("condicion no reconocida")    
    
numero = int(input("Proporciona un numero entre 1 y 3:"))  
if numero == 1:
    numeroTexto = "número uno"
elif numero == 2:
    numeroTexto = "número dos"   
elif numero == 3:
    numeroTexto = "número tres" 
else:
    numeroTexto = "Valor fuera de rango"  
    
print("numero proporcionado:",numeroTexto)    
