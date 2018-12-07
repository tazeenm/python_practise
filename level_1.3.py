'''
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that i is an integral number between 1 and n (both included). 
And then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''

def dictionary(x):
    new_dict = dict()
    #print(type(dict))

    for i in range(1, x+1):
        new_dict[i] = i*i

    print(new_dict)

if __name__ == '__main__':
    n = int(input("Enter the stop range: "))
    dictionary(n)
