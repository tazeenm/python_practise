'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
import os
import sys

#Main Class
class MainClass:
    #Method that gets the string from console input
    def ConsoleString(self, testString):
        return testString

    #Method that prints the string from console input to uppercase
    def UpperCaseString(self, upperString):
        return upperString.upper()

    #Test function to test the two methods
    def testFunc(self, x, y):
        str1 = self.ConsoleString(x)
        str2 = self.UpperCaseString(y)

        print(str1)
        print(str2)

if __name__ == "__main__":
    #Console input - first string returns the string as it is and the second string prints in upper case
    x = input("Enter first string: ")
    y = input("Enter second string: ")
    
    obj1 = MainClass()
    obj1.testFunc(x, y)
    