#Multilevel Inheritance

class GrandFather:
    gold = "1kg"
    def bhk1(self):
        print("1BHK")

class Father(GrandFather):
    gold = "2kg"
    def bhk2(self):
        print("1BHK")
class Son(Father):
    gold = "3kg"
    def bhk3(self):
        print("1BHK")

g = GrandFather()
f = Father()
s = Son()

s.bhk1()