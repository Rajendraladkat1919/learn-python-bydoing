# check the grade of the student and provide the remark for the same.


grade = int(input("Please provide your grade."))

if grade >=60:
    print("You are doing good: ")
elif grade >= 55 and grade < 60:
    print("Little hard work needed.")
else:
    print("No worries. Hard work is key to success.")
