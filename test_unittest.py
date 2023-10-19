import unittest

# Classe de exemplo para testes
class Calculadora:
    def soma(self, a, b):
        return a + b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

    def subtracao(self, a, b):
        return a - b

    def igualdade(self, a, b):
        return a == b

# Classe de teste para a Calculadora
class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_soma(self):
        resultado = self.calculadora.soma(5, 3)
        self.assertEqual(resultado, 8)  # Oráculo 1: Verifica se 5 + 3 é igual a 8
        self.assertTrue(resultado > 0)  # Oráculo 2: Verifica se o resultado é positivo

    def test_multiplicacao(self):
        resultado = self.calculadora.multiplicacao(4, 6)
        self.assertEqual(resultado, 24)  # Oráculo 1: Verifica se 4 * 6 é igual a 24
        self.assertTrue(resultado % 2 == 0)  # Oráculo 2: Verifica se o resultado é par

    def test_divisao(self):
        resultado = self.calculadora.divisao(10, 2)
        self.assertEqual(resultado, 5.0)  # Oráculo 1: Verifica se 10 / 2 é igual a 5.0
        self.assertFalse(resultado == 0)  # Oráculo 2: Verifica se o resultado não é igual a zero

    def test_subtracao(self):
        resultado = self.calculadora.subtracao(9, 4)
        self.assertEqual(resultado, 5)  # Oráculo 1: Verifica se 9 - 4 é igual a 5
        self.assertTrue(resultado >= 0)  # Oráculo 2: Verifica se o resultado é maior ou igual a zero

    def test_igualdade(self):
        resultado = self.calculadora.igualdade(7, 7)
        self.assertTrue(resultado)  # Oráculo 1: Verifica se 7 é igual a 7
        resultado = self.calculadora.igualdade(5, 8)
        self.assertFalse(resultado)  # Oráculo 2: Verifica se 5 é diferente de 8

if __name__ == '__main__':
    unittest.main()
