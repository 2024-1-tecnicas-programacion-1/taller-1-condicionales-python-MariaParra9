import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.ordenamiento import evaluar

class TestOrdenamiento(unittest.TestCase):
    def testNo(self):
        valor_esperado = "Los números ordenados de menor a mayor son: 0 1 6 7"
        valor_actual = evaluar(7, 0, 6, 1)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testAscendente(self):
        valor_esperado = "Los números ordenados de menor a mayor son: 1 2 3 4"
        valor_actual = evaluar(1, 2, 3, 4)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDescendente(self):
        valor_esperado = "Los números ordenados de menor a mayor son: 1 2 3 4"
        valor_actual = evaluar(4, 3, 2, 1)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testNegativos(self):
        valor_esperado = "Los números ordenados de menor a mayor son: -4 -2 1 3"
        valor_actual = evaluar(-2, 3, 1, -4)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testIguales(self):
        valor_esperado = "Los números ordenados de menor a mayor son: 5 5 5 5"
        valor_actual = evaluar(5, 5, 5, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testUnoNegativo(self):
        valor_esperado = "Los números ordenados de menor a mayor son: -4 1 3 5"
        valor_actual = evaluar(1, 3, 5, -4)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testTodosNegativos(self):
        valor_esperado = "Los números ordenados de menor a mayor son: -5 -4 -3 -1"
        valor_actual = evaluar(-4, -3, -5, -1)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testTodosCero(self):
        valor_esperado = "Los números ordenados de menor a mayor son: 0 0 0 0"
        valor_actual = evaluar(0, 0, 0, 0)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testAlgunoCero(self):
        valor_esperado = "Los números ordenados de menor a mayor son: -3 0 1 4"
        valor_actual = evaluar(-3, 1, 0, 4)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testRandom(self):
        valor_esperado = "Los números ordenados de menor a mayor son: -9 0 2 7"
        valor_actual = evaluar(2, 7, -9, 0)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
