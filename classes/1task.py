class printer:
    def __init__(self):
        self.text = ""
    def getString(self):
        self.text = input()
    def printString(self):
        print(self.text.upper())

Printer = printer()
Printer.getString()
Printer.printString()
