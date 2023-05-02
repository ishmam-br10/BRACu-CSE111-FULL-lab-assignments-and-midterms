class Calculator:
    def __init__(self):
        print("Calculator is ready !")
    def calculate(self, number1, number2, operator):
        self.num1 = number1
        self.num2 = number2
        self.ope = operator
        if self.ope == '+':
            value = self.num1 + self.num2
            return value
        elif self.ope == '-':
            value = self.num1 - self.num2
            return value
        elif self.ope == '*':
            value = self.num1 * self.num2
            return value
        elif self.ope == '/':
            value = self.num1 / self.num2
            return (f"{value: .2f}")
    def showCalculation(self):
        print(f"{self.num1} {self.ope} {self.num2} = {self.calculate(self.num1, self.num2, self.ope)}")
# DRIVER CODE

c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()
