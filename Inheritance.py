from Oops import Calculator


class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)    # Syntax to inherit parent class constructor with variable values

    def getCompleteData(self):
        return self.num + self.num2 + self.summation()


obj = Child()        # you can give values here also to execute when constructor is not mentioned
print(obj.getCompleteData())
