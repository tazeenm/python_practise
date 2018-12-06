'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

#Main Function
if __name__ == '__main__':
    num = int(input("Enter a number: "))
    #print(num)
    res = fact(num)
    print(res)