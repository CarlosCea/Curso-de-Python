print("Proporcione los siguientes datos del libro:")
nombre = input("Proporcione el nombre:")
id = int(input("Proporcione el ID:"))
precio = float(input("proporcione el precio:"))
envioGratuito = input("indica si el envio es gratuito(True/False):")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False    
else:
    envioGratuito = "Valor incorrecto, debe ser True/False"  

print("Nombre:", nombre) 
print("id:", id) 
print("Precio", precio) 
print("Envio Gratuito?:", envioGratuito) 
print(type(envioGratuito))  