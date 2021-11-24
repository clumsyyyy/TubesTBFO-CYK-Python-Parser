class Something:
    def __init__(self, a, b):
        Something.a **= Something.b
        Something.b = b 
        return "Nice"
    def printHello(self):
        print("hello world")

aString = Something()
aString.printHello()
