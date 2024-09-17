# problem to find the max between three no

a = int(input("Enter the number\n"))
b = int(input("Enter the number\n"))
c = int(input("Enter the number\n"))

if a > b > c:
    print("Max. No. is", a)
elif b > a > c:
    print("Max no. is", b)
else:
    print("Max No. is", c)
