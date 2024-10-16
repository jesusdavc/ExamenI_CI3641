#CI 3641 Lenguajes de Programación I
#Estudiante Jesús Cuéllar Carnet 15-10345
#Pregunta 3 
#Pruebas Unitarias con unittest
from modulo_cuaternion import Cuaternion
import unittest
import math

q1 = Cuaternion(1,2,3,4)
q2 = Cuaternion(8,7,6,5)
scalar = 3
#Usamos la libreria unittest. 
#Leyendo la documentación aplicamos las siguientes pruebas de cada operación del modulo de Cuaternion
class TestCuartionFunction(unittest.TestCase):
    #Prueba 1: Operación suma de dos Cuaterniones
    def test_add(self):
        q3 = q1 + q2
        self.assertEqual( q3.a , (q1.a + q2.a))
        self.assertEqual( q3.b , (q1.b + q2.b))
        self.assertEqual( q3.c , (q1.c + q2.c))
        self.assertEqual( q3.d , (q1.d + q2.d))
    #Prueba 2: Operación suma de un Cuaternion y un escalar
    def test_add_scalar(self):
        q3 = q1 + scalar
        self.assertEqual( q3.a , (q1.a + scalar))
        self.assertEqual( q3.b , (q1.b))
        self.assertEqual( q3.c , (q1.c))
        self.assertEqual( q3.d , (q1.d))
    #Prueba 3 Operación multiplicación de un Cuaternion y un Cuaternion
    def test_mul(self):
        q3 = q1 * q2
        self.assertEqual( q3.a , (q1.a*q2.a - q1.b*q2.b - q1.c*q2.c - q1.d*q2.d ))
        self.assertEqual( q3.b , (q1.a*q2.b + q1.b*q2.a + q1.c*q2.d - q1.d*q2.c ))
        self.assertEqual( q3.c , (q1.a*q2.c - q1.b*q2.d + q1.c*q2.a + q1.d*q2.b ))
        self.assertEqual( q3.d , (q1.a*q2.d + q1.b*q2.c - q1.c*q2.b + q1.d*q2.a ))
    #Prueba 4 Operación multiplicación de un Cuaternion y un escalar
    def test_mul_scalar(self):
        q3 = q1 * scalar
        self.assertEqual( q3.a , (q1.a * scalar))
        self.assertEqual( q3.b , (q1.b * scalar))
        self.assertEqual( q3.c , (q1.c * scalar))
        self.assertEqual( q3.d , (q1.d * scalar))
    #Prueba 5 Operación Conjungada
    def test_conjugada(self):
        q3 = ~q1
        self.assertEqual( q3.a ,  (q1.a))
        self.assertEqual( q3.b , -(q1.b))
        self.assertEqual( q3.c , -(q1.c))
        self.assertEqual( q3.d , -(q1.d))
    #Prueba 6 Operación norma
    def test_norma(self):
        q3 = +q1
        self.assertEqual(q3, math.sqrt(q1.a**2 + q1.b**2 + q1.c**2 + q1.d**2))

if __name__ == '__main__':
    unittest.main()