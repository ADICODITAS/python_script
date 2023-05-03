# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return “empty string”.
string=input("enter a string")
count=0
str=len(string)
if str>2:
    for i in string[0:2]:
        print(i,end="")
    for i in string[-1:-3:-1]:
         print(i,end="")   