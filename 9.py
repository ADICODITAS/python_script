#Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.
def check(number1,number2):
    if number1%number2==0:
        print("number is divisible")
    else:
        print("not divisible ")

number1=int(input("enter the number "))
number2=int(input("enter the number by which you want to divide "))

check(number1,number2)