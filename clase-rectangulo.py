class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
        
    def calcula_area (self):
        return self.base * self.altura
    
    def calcula_area1(self):
        return self.base1 * self.altura1
    
#base = int(input("Proporciona la base:"))
#altura = int(input("Proporciona la altura:"))

#base1 = int(input("Proporciona la base1:"))
#altura1 = int(input("Proporciona la altura1:")) 
 
 
    
#Crear el objeto
rectangulo = Rectangulo(1, 2)
print("El resultado del area1 es:", rectangulo.calcula_area())
print(id(rectangulo))

rectangulo1 = Rectangulo(3, 4)
print("El resultado del area2 es:", rectangulo1.calcula_area())
print(id(rectangulo1))

        