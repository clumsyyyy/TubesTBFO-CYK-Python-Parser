class Something:
    def __init__(self, a, b):
        Something.a = a
        Something.b = b 
        return "Nice"
    def printHello(self):
        print("hello world")

aString = Something()
aString.printHello()
