#Inheritance
#Singal Inheritance

class Father:
    key = "2bhk"
    def my_home(self):
        print("Home",self.key)

class Son(Father):
    pass
object = Father()
object.my_home()

object1 = Son()
object1.my_home()