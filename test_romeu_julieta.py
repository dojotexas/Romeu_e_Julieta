# Importando o modulo de unittest
import unittest
# Importando o nosso Programa com o nome app importando o metodo Romeu e Julieta
from app import romeu_julieta

class TestRomeuJulieta(unittest.TestCase):
    def test_valor1(self):
    	self.assertEqual(romeu_julieta(1),'1')
    def test_queijo(self):
    	self.assertEqual(romeu_julieta(3),'queijo')
    def test_valor4(self):
    	self.assertEqual(romeu_julieta(4),'4')
    def test_goiabada(self):
    	self.assertEqual(romeu_julieta(5),'goiabada')
    def test_romeujulieta(self):
    	self.assertEqual(romeu_julieta(15), 'Romeu e Julieta')
    def test_romeujulieta30(self):
    	self.assertEqual(romeu_julieta(30), 'Romeu e Julieta')

if __name__== '__main__':
    unittest.main()
