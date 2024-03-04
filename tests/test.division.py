import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.division import evaluar

class TestDivision(unittest.TestCase):
    def testDivisionExacta(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 2\n" \
                         "Residuo: 4"
        valor_actual = evaluar(14, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionNoExacta(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 0\n" \
                         "Residuo: 3"
        valor_actual = evaluar(10, 3)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionPorCero(self):
        valor_esperado = "No se puede dividir con 0"
        valor_actual = evaluar(10, 0)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionNegativa(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: -3\n" \
                         "Residuo: 0"
        valor_actual = evaluar(-12, 4)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionFraccionaria(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 0\n" \
                         "Residuo: 0"
        valor_actual = evaluar(0, 3)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionGrande(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 10000\n" \
                         "Residuo: 0"
        valor_actual = evaluar(100000, 10)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionDecimal(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 2\n" \
                         "Residuo: 0"
        valor_actual = evaluar(0, 2.5)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionDecimalesGrandes(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 1000000\n" \
                         "Residuo: 0"
        valor_actual = evaluar(2500000, 2.5)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionDecimalesNegativos(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: -1000000\n" \
                         "Residuo: 0"
        valor_actual = evaluar(-2500000, 2.5)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionDecimalesNegativos2(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: -1000000\n" \
                         "Residuo: 0"
        valor_actual = evaluar(-2500000, -2.5)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
