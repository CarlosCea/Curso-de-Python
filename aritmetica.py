class Aritmetica:
    """Clase Aritmetica para realizar las operaciones de sumar, restar, etc"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.operando1 + self.operando2 
    
    def resta(self):
        return self.operando1 - self.operando2
    
    def multiplica(self):
        return self.operando1 * self.operando2
    
    def divicion(self):
        return self.operando1 / self.operando2
    
    
# Creamos un objeto        
aritmetica = Aritmetica(2, 4)
print("El resultado de la suma es: ", aritmetica.sumar())

aritmetica2 = Aritmetica(4, 2)
print("el resultado de la resta es: ", aritmetica2.resta())

aritmetica3 = Aritmetica(3, 2)
print("El resultado de la multiplicacion es: ", aritmetica3.multiplica())

aritmetica4 = Aritmetica(20, 2)
print("El resultado de la divicion es:", aritmetica4.divicion())