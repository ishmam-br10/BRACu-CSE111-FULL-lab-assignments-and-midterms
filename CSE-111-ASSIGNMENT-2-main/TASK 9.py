class buttons():
    def __init__(self, word, spaces, border):
        self.word = word
        self.spaces = spaces
        self.border = border
        number = 1 + int(spaces) + len(word) + int(spaces) + 1
        print(f"{self.border * number}")
        print(border+" "*spaces+word+" "*spaces+border,sep="")
        print(f"{self.border * number}")

# DRIVER CODE
word = "CANCEL"
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')