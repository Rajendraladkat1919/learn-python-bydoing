# Python3 code to demonstrate working of
# Remove square brackets from list

# initialize list
test_list = [5, 6, 8, 9, 10, 21]

# printing original list
print("The original list is : " + str(test_list))

# Remove square brackets from list
x=str(test_list)
x=x.replace("[","")
x=x.replace("]","")
# printing result
print("List after removing square brackets : " + x)
