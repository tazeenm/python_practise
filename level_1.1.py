'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

list_num=[]
for i in range(2000, 3200+1):
    if((i%7 == 0) and (i%5 != 0)):
        list_num.append(str(i))

#Prints in a comma separated sequence
print(','.join(list_num))

#print(list_num) - prints in a list format