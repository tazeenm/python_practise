'''
Write a program that accepts a comma separated sequence of words as input 
and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
Example: 
without,hello,bag,world
Output:
bag,hello,without,world
'''

print("Enter the words: ")
user_input = input()
words = user_input.split(",")
print("Unsorted: ", words)
#print(type(words))

sorted_words = sorted(words)

print("Sorted: ", sorted_words)



