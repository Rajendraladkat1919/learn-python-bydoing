

age=int(input("Please enter the age.: "))

if age > 18:
    print("You are eligible")
    if age >=18 and age <=65:
        print("Yes. Please drive carefully.")
    else:
        print("You are not eligible to drive alone.")
else:
    print("Wait till you turn 18.")