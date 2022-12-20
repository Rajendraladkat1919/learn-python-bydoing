

# check the type of given variable.

a= 5

b= "Rajendra"

f= 10.5

c= True


# Use case 0.

if type(a) == int:
    print("Value of a is Integer.",end="\n\n" )


# Use case 1
print("I am from the first use case",end="\n")
if type(b) == "string" and str:
    print(type(b)==str)
    print(type(b) == 'string')
    print("No. I will not going to print myself at all.")
 
print("\n")
# use case 2


if type(b) == "string" or str:
    print(type(b)==str)
    print(type(b) == 'string')
    print("Yes. This is also the case of if.")

print("\n")
print("Oh sorry use case 2 will not execute.")