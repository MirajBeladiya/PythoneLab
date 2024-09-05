# # write  a program that calcultes and display  the latter grade
# # for given numerical score
# # based on the following grading scale:
#
# # A--90-100
# # b- 80-89
# c -70-79
# d- 60-69
# f-0-59

Score = int(input("Enter your score\n"))
grade = "F"

if Score >= 90 and Score <= 100:
    grade = "A"
    print("your grade is", grade)
elif Score >= 80 and Score <= 89:
    grade = "B"
    print("your grade is", grade)
elif Score >= 70 and Score <= 79:
    grade = "C"
    print("your grade is", grade)
elif Score >= 60 and Score <= 69:
    grade = "D"
    print("your grade is", grade)
elif Score >= 0 and Score <= 59:
    grade = "E"
    print("your grade is", grade)
else:
    grade = "F"
    print("your grade is", grade)
