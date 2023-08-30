class Parent:
    num=100
    num1=200

    def addition(self):
        result = self.num + self.num1
        return result


class child(Parent):
    def multiplication(self):
        result1 = self.num* self.num1
        return result1


obj = child()
print(obj.addition())


list = ["basic","synechron","India"]
print(len(list[1]))