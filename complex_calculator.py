import logging
import unittest

# Настройка логирования
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

class Operations:
    @staticmethod
    def add(c1: ComplexNumber, c2: ComplexNumber) -> ComplexNumber:
        result = ComplexNumber(c1.real + c2.real, c1.imaginary + c2.imaginary)
        logging.info(f"Adding: {c1} + {c2} = {result}")
        return result

    @staticmethod
    def multiply(c1: ComplexNumber, c2: ComplexNumber) -> ComplexNumber:
        real = c1.real * c2.real - c1.imaginary * c2.imaginary
        imaginary = c1.real * c2.imaginary + c1.imaginary * c2.real
        result = ComplexNumber(real, imaginary)
        logging.info(f"Multiplying: {c1} * {c2} = {result}")
        return result

    @staticmethod
    def divide(c1: ComplexNumber, c2: ComplexNumber) -> ComplexNumber:
        denom = c2.real ** 2 + c2.imaginary ** 2
        real = (c1.real * c2.real + c1.imaginary * c2.imaginary) / denom
        imaginary = (c1.imaginary * c2.real - c1.real * c2.imaginary) / denom
        result = ComplexNumber(real, imaginary)
        logging.info(f"Dividing: {c1} / {c2} = {result}")
        return result

class Calculator:
    def __init__(self):
        self.operations = Operations()

    def add(self, c1: ComplexNumber, c2: ComplexNumber) -> ComplexNumber:
        return self.operations.add(c1, c2)

    def multiply(self, c1: ComplexNumber, c2: ComplexNumber) -> ComplexNumber:
        return self.operations.multiply(c1, c2)

    def divide(self, c1: ComplexNumber, c2: ComplexNumber) -> ComplexNumber:
        return self.operations.divide(c1, c2)

# Тесты
class TestOperations(unittest.TestCase):
    def test_add(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(3, 4)
        result = Operations.add(c1, c2)
        self.assertEqual(result.real, 4)
        self.assertEqual(result.imaginary, 6)

    def test_multiply(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(3, 4)
        result = Operations.multiply(c1, c2)
        self.assertEqual(result.real, -5)
        self.assertEqual(result.imaginary, 10)

    def test_divide(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(3, 4)
        result = Operations.divide(c1, c2)
        self.assertAlmostEqual(result.real, 0.44, places=2)
        self.assertAlmostEqual(result.imaginary, 0.08, places=2)

if __name__ == '__main__':
    # Запуск тестов
    unittest.main(exit=False)
    
    # Пример использования калькулятора
    calc = Calculator()
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)
    
    print(f"{c1} + {c2} = {calc.add(c1, c2)}")
    print(f"{c1} * {c2} = {calc.multiply(c1, c2)}")
    print(f"{c1} / {c2} = {calc.divide(c1, c2)}")
