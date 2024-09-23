# TRY , Except, finally

print("--Start of the program--")
try:
    a = int(input("Enter he num1"))
    b = int(input("Enter he num1"))
    c = a / b
except ValueError as ve:
    print("Valur error, you entred the sting instand of we want int")
except ZeroDivisionError as z:
    print("Zero div error dont put zero in ")
else:
    print(f"c={c}")
finally:
    print("this code always be excuted")