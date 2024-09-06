# Match statement
# switch in java
# Match the o/p and excute

# syntax
#
# match variable:
#     case pattern1:
#     case pattern2:

# write a program to ask the user which browser he want to run automation

browser_name = input("Enter the browser name\n")
browser_name = browser_name.lower()

match browser_name:
    case "firefox":
        print("Excute firefox code")
    case "chrome":
        print("Excute chrome code")
    case _:
        print("Browser not found")
