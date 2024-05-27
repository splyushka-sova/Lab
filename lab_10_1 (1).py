class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class ExtendedCalculator (BasicCalculator):

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b



calculator = ExtendedCalculator()
print("Addition: ", calculator.add(5, 3))
print("Subtraction: ", calculator.subtract(5, 3))
print("Multiplication: ", calculator.multiply(5, 3))
print("Division: ", calculator.divide(5, 3))
