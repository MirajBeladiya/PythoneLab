# Encapsulation

class My_class:
    #public variable (Instance)
    public_var = "I am Public"

    #Private Variable
    __private_var = "I am private"

    #Protected variable
    _protected_var = "I am protected"

object1 = My_class()
print(object1.public_var)
#print(object1.__private_var) can not access private variable
print(object1._protected_var)
