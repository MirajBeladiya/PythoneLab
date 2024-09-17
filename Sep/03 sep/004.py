class Car:

    def __init__(self,name, modal, o_make):
        self.name = name
        self.modal = modal
        self.o_make = o_make

    def print_all(self):
        print("Name" + self.name)
        print("modal" + self.modal)
        print("Name" + self.o_make)

object1 = Car("Thar", "v", "2024")
object1.print_all()