import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.imc import evaluar

class TestIMC(unittest.TestCase):
    def testBajo(self):
        valor_esperado = "Bajo"
        valor_actual = evaluar(50, 1.8, 20)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testMedio1(self):
        valor_esperado = "Medio"
        valor_actual = evaluar(60, 1.75, 35)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testMedio2(self):
        valor_esperado = "Medio"
        valor_actual = evaluar(70, 1.7, 40)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testAlto(self):
        valor_esperado = "Alto"
        valor_actual = evaluar(80, 1.65, 50)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testBajoEdgeCase(self):
        valor_esperado = "Bajo"
        valor_actual = evaluar(45, 1.8, 44)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testMedio1EdgeCase(self):
        valor_esperado = "Medio"
        valor_actual = evaluar(70, 1.75, 44)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testMedio2EdgeCase(self):
        valor_esperado = "Medio"
        valor_actual = evaluar(90, 1.7, 45)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testAltoEdgeCase(self):
        valor_esperado = "Alto"
        valor_actual = evaluar(95, 1.65, 55)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testBajoUpperBound(self):
        valor_esperado = "Bajo"
        valor_actual = evaluar(35, 1.8, 44)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testAltoLowerBound(self):
        valor_esperado = "Alto"
        valor_actual = evaluar(100, 1.65, 45)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
