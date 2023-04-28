#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
number1=float(input("enter the first number"))
number2=float(input("enter the second number"))
if number1==number2:
    print("True")
elif number1+number2==5:
    print("True")
elif number1-number2==5 or number2-number1==5:
    print("True")

else:
    print("False")