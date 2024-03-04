import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.annos_bisiestos import evaluar

class TestAnnosBisiestos(unittest.TestCase):
    def test_1988(self):
        valor_esperado = "1988 es bisiesto"
        valor_actual = evaluar(1988)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_2000(self):
        valor_esperado = "2000 es bisiesto"
        valor_actual = evaluar(2000)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_2020(self):
        valor_esperado = "2020 es bisiesto"
        valor_actual = evaluar(2020)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_1600(self):
        valor_esperado = "1600 es bisiesto"
        valor_actual = evaluar(1600)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_1800(self):
        valor_esperado = "1800 no es bisiesto"
        valor_actual = evaluar(1800)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_1900(self):
        valor_esperado = "1900 no es bisiesto"
        valor_actual = evaluar(1900)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_2100(self):
        valor_esperado = "2100 no es bisiesto"
        valor_actual = evaluar(2100)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_2200(self):
        valor_esperado = "2200 no es bisiesto"
        valor_actual = evaluar(2200)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_2400(self):
        valor_esperado = "2400 es bisiesto"
        valor_actual = evaluar(2400)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_2300(self):
        valor_esperado = "2300 no es bisiesto"
        valor_actual = evaluar(2300)
        self.assertEqual(valor_esperado, valor_actual)


if __name__ == '__main__':
    unittest.main()
