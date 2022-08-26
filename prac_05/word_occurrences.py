"""
CP1404/CP5632 Practical
Program to count the occurrences of words in a string
GitHub: https://github.com/XD2013/cp1404practicals
"""

counted_word = {}
text = input("Text: ")

words = text.split()
for word in words:
    frequency = counted_word.get(word, 0)
    counted_word[word] = frequency + 1
print(counted_word)
words = list(counted_word.keys())
words.sort()
# length = max((len(word) for word in words))
# for word in words:
#     print("{:{}}  :  {}".format(word, length, counted_word[word]))
for word in words:
    print(f"{word:<15}:  {counted_word[word]}")
