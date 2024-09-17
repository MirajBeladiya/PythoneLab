# Take user input and creat class in python
class Person:
    def __init__(self):
        self.name = input("Enter your name\n")
        self.age = input("Enter your age\n")
        self.phoneno = input("Enter your phoneno\n")

    def name_of_the_function(self):
        print(f"Name is {self.name}")
        print(f"age is {self.age}")
        print(f"phoneno is {self.phoneno}")

# Create an object
person1 = Person()
# call the display function
person1.name_of_the_function()


