# User defined
# 1. they can't return --> non return
# 2. they can return somthing
# 3. They have parameters.
# 4. They dont parameter/arguments

# 1. they can't return --> non return
# No return type no parameter
def greet():
    print("Hello")


result = greet()
print(result)


# 2. they can return somthing
# No return type and with argument
def greet_by_name(name):
    print("Hello", name)


greet_by_name("Miraj")


# 3 No return type with default argument
def greet_by_name(name="Miraj"):
    print("Hello", name)


greet_by_name()


# Argument with return type

def sum_of_two_number(num1, num2):
    return num1 + num2


result = sum_of_two_number(num1=20, num2=20)
print(result)
