class RealNumber:

    def __init__(self, r=0):
        self.__realValue = r

    def getRealValue(self):
        return self.__realValue

    def setRealValue(self, r):
        self.__realValue = r

    def __str__(self):
        return 'RealPart: ' + str(self.getRealValue())
## WRITE FROM HERE
class ComplexNumber(RealNumber):
    def __init__(self, real = 1, complex = 1):
        super().__init__(float(real))
        self.complex = float(complex)
    def __str__(self):
        return f"{super().__str__()}\nImaginaryPart: {self.complex}"

cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5, 7)
print(cn2)