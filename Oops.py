class Calculator:
    num = 100

    def __init__(self):          # syntax to create constructor
        print("This default constructor is created and called automatically when object is created")

    def __init__(self, a, b):
        self.fn = a
        self.sn = b
        print("Parameterized constructor is called instead of default constructor since it is declared")

    def getData(self):
        print("Method in class")

    def summation(self):
        return self.fn + self.sn + obj.num      # instance variables calling using self keyword


obj = Calculator(2, 3)           # syntax to create object of class
obj.getData()
print(obj.summation())

obj = Calculator(5, 5)
obj.getData()
print(obj.summation())
