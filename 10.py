# Write a Python program to count the number of characters (character frequency) in a string
def count_characters(string):
    char_counts={}

    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
string = "aditaya"
char_counts = count_characters(string)
print(char_counts)
