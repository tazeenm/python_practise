'''
Write a program which accepts a sequence of comma-separated numbers from the console 
and generates a list and a tuple which contains those numbers.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''

n = input("Enter the stop range: ")
print("Enter {} values separated by a comma".format(n))
user_input = input()
#To accept number sequences that are comma separated from the console
values = user_input.split(",")
#List
print("List: ", values)
#Tuple
new_tuple = tuple(values)
print("Tuple: ", new_tuple)
