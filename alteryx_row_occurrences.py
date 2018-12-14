'''
A Python Script that takes an excel sheet as input and returns the number of duplicates as well as the number of occurrences of each row
'''

import pandas as pd
import xlrd

file = 'test.xlsx'
xlsx = pd.ExcelFile(file)

df = pd.read_excel(xlsx, 'Sheet1')
cols = df.columns

print(df.columns)

df['is_duplicated'] = df.duplicated(cols)

#Prints the number of duplicates in the file
x = df['is_duplicated'].sum()
print(x)

df['duplicate_occurrences'] = df.groupby(list(cols)).name.cumcount()
df[df.duplicated(subset=cols)]
print (df)