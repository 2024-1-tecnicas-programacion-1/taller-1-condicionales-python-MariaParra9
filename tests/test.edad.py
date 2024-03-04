import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.edad import evaluar

class TestEdad(unittest.TestCase):
    def test2000Enero1(self):
        valor_esperado = "Usted tiene 24 años"
        valor_actual = evaluar(1, 1, 2024)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test1990Julio15(self):
        valor_esperado = "Usted tiene 33 años"
        valor_actual = evaluar(15, 7, 1990)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test1975Febrero28(self):
        valor_esperado = "Usted tiene 49 años"
        valor_actual = evaluar(28, 2, 1975)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test1988Septiembre30(self):
        valor_esperado = "Usted tiene 36 años"
        valor_actual = evaluar(30, 9, 1988)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test2025Marzo8(self):
        valor_esperado = "Vas a cumplir 3 años"
        valor_actual = evaluar(8, 3, 2025)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test2003Diciembre25(self):
        valor_esperado = "Cumpliste 18 años"
        valor_actual = evaluar(25, 12, 2003)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test1999Abril1(self):
        valor_esperado = "Usted acaba de cumplir 23 años"
        valor_actual = evaluar(1, 4, 1999)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test1985Junio10(self):
        valor_esperado = "Cumpliste 36 años"
        valor_actual = evaluar(10, 6, 1985)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test2026Noviembre20(self):
        valor_esperado = "Vas a cumplir 2 años"
        valor_actual = evaluar(20, 11, 2026)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test2000Enero1LeapYear(self):
        valor_esperado = "Usted tiene 24 años"
        valor_actual = evaluar(1, 1, 2000)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
