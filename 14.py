#Write a Python program to count the occurrences of each word in a given sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
        print("word")
    else:
        word_counts[word] = 1

# print the word counts
for word, count in word_counts.items():
    print(word, count)
