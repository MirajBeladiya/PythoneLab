#Constructor

class Dog:
    name = None
    age = None

    def __init__(self,name,age):#Constructor
        print("automatically called")
        self.name = name
        self.age = age

    def sleep(self):
        print("Sleeping")

dog1 = Dog("kuch bhi",10)
print(dog1.name)
print(dog1.age)