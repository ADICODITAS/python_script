# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
def sum_of_three(a, b, c):
    if a == b == c:
        return 3 * (a + b + c)
    else:
        return a + b + c

numbers = []
for i in range(3):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)

result = sum_of_three(numbers[0], numbers[1], numbers[2])

print(f"The sum of {numbers[0]}, {numbers[1]}, and {numbers[2]} is {result}.")