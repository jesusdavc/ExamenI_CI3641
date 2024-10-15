#CI 3641 Lenguajes de Programación I
#Estudiante Jesús Cuéllar Carnet 15-10345
#Pregunta 3 

import math #Importamos math para usar los símbolos

#Definimos la clase Cuartenion. Con las operaciones necesarias. 
#Para poder aplicar estas operaciones aplicamos sobrecarga. 
#En Python se hace modificando
#ciertos operadores.
#Este articulo en Medium puede dar más info.
#https://medium.com/@LuisMBaezCo/overloading-sobrecargar-operadores-en-python-5d7a75e2bfdf

class Cuaternion:
    def __init__(self, a, b=0, c=0, d=0):
        self.a = a  # parte real
        self.b = b  # coeficiente de i
        self.c = c  # coeficiente de j
        self.d = d  # coeficiente de k

    # Suma de cuaterniones
    def __add__(self, other):
        if isinstance(other, Cuaternion):
            return Cuaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
        elif isinstance(other, (int, float)):
            return Cuaternion(self.a + other, self.b, self.c, self.d)
        else:
            raise TypeError("Operación no soportada para el tipo")

    # Producto de cuaterniones
    def __mul__(self, other):
        if isinstance(other, Cuaternion):
            a1, b1, c1, d1 = self.a, self.b, self.c, self.d
            a2, b2, c2, d2 = other.a, other.b, other.c, other.d
            return Cuaternion(
                a1*a2 - b1*b2 - c1*c2 - d1*d2,
                a1*b2 + b1*a2 + c1*d2 - d1*c2,
                a1*c2 - b1*d2 + c1*a2 + d1*b2,
                a1*d2 + b1*c2 - c1*b2 + d1*a2
            )
        elif isinstance(other, (int, float)):
            return Cuaternion(self.a * other, self.b * other, self.c * other, self.d * other)
        else:
            raise TypeError("Operación no soportada para el tipo")

    # Conjugada de un cuaternión
    def __invert__(self):
        return Cuaternion(self.a, -self.b, -self.c, -self.d)

    # Valor absoluto (norma)
    #Acá toca aclarar que el operador & es un operador unario
    #por lo que lo sustituimos y usamos +como operador unario
    #esto para poder hacer la sobre carga.
    def __pos__(self):
        return math.sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)

    # Representación del cuaternión como string
    def __repr__(self):
        return f"({self.a} + {self.b}i + {self.c}j + {self.d}k)"

# Pruebas
q1 = Cuaternion(1, 2, 3, 4)
q2 = Cuaternion(2, -1, 0, 3)

q3 = q1*3 +1

print(q3)
