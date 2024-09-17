# Instance variable

class Person:
    # Instance variable
    name = "Miraj"  # Hardcode value

    def __init__(self, name):  # so thats why we use constructor to use global variable
        self.name = name       # change the value

    def print_name(self):
        #print(self.name)
        return self.name


object1 = Person("Bubu")
object1.print_name()
print(object1.name)