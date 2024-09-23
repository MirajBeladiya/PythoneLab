print("--Start of the program--")
try:
    a = int(input("Enter he num1"))      #ValueError: invalid literal for int() with base 10: 'miraj'
    b = int(input("Enter he num1"))
    c = a / b                            #ZeroDivisionError: division by zero
    print("result",c)
except Exception as q:
    print(q)

print("--End of the program--")
