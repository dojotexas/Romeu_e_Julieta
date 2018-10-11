# Importando o modulo de unittest
import unittest
# Importando o nosso Programa com o nome app importando o metodo Romeu e Julieta
from app import romeu_julieta

class TestRomeuJulieta(unittest.TestCase):
    def test_multiplo3(self):
    	self.assertEqual(romeu_julieta(3),'Queijo')
    def test_multiplo5(self):
        self.assertEqual(romeu_julieta(5),'Goiabada')
    def test_multiplo3and5(self):
        self.assertEqual(romeu_julieta(15),'Romeu e Julieta')
    def test_difrente3or(self):
        self.assertEqual(romeu_julieta(1),1)
    def test_diferenteValor(self):
        self.assertEqual(romeu_julieta(23948734986734987256),"Queijo")

if __name__== '__main__':
    unittest.main()
