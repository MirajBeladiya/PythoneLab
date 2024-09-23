import math
try:
    math.exp(1000) #OverflowError: math range error
except Exception as q:
    print(q)
    print("if error will ocuur show the message")