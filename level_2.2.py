'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''

user_input = input("Enter dimensions of 2-D array: ")
w, h = user_input.split(",")
#print(type(w))
row = int(w)
col = int(h)
x = [[0 for i in range(col)] for j in range(row)]

#print(x)

for i in range(row):
    for j in range(col):
        x[i][j] = i * j

print(x)
