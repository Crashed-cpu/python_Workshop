class Calculator:
    def add(self, a, b):
        return a + b
        

    def sub(self, a, b):
        return a - b
        

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b
        

    def rem(self, a, b):
        return a % b

calc = Calculator()

print(calc.add(20, 5))
print(calc.sub(20, 5))
print(calc.mul(20, 5))
print(calc.div(20, 5))
print(calc.rem(20, 5))