# Write a Python program to test whether a number is within 100 of 1000 or 2000.
number=float(input("enter number"))
if number<100:
    print("less than 100")
elif number>100 and number<1000:
    print("number is between 100 and 1000 ")
elif number>1000 and number<2000:
    print("number is between 1000 and 2000 ")
else:
    print("number is greater than 2000")