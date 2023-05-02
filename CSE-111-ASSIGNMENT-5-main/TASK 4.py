class Color:
    def __init__(self, colour):
        self.clr = colour

    def __add__(self, other):
        res = self.clr + other.clr
        if res == 'redyellow' or res == 'yellowred':
            return Color('Orange')
        elif res == 'redblue' or res == 'bluered':
            return Color('Violet')
        elif res == 'yellowblue' or res == 'blueyellow':
            return Color('Green')
# DRIVER
C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)
