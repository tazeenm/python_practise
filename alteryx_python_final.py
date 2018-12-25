'''
A Python Script that takes an excel sheet as input and returns the number of duplicates as well as the number of occurrences of each row
'''

import pandas as pd
import xlrd
import numpy as np

#Input file (to be taken from alteryx workflow)
#Alteryx.read("#1")
input_file = 'test.xlsx'
xlsx = pd.ExcelFile(input_file)
df1 = pd.read_excel(xlsx, 'Sheet1')

input_cols = df1.columns

'''
Compare filename and ignore the fields
'''

# Add the Parameter file path here
parameter_file = r'C:\Users\Tazeen.Munnavar\OneDrive\Documents\Alteryx\Critical Reports\User_Parameter.xlsx'
xlsx1 = pd.ExcelFile(parameter_file)
df2 = pd.read_excel(xlsx1, 'Sheet1')
param_cols = df2.columns

row_values = df2[['Column','Ignore']]
print("Row Values: \n", row_values)

column_headers = list(input_cols)

col_name = list(set(input_cols).intersection(row_values['Column']))
print("Common Columns: ", col_name)
df3 = pd.Series(col_name).astype(bool)


ignore_col1 =  row_values['Ignore'].str.contains('Yes')
print("Columns to ignore:\n", df3)
df4 = pd.Series(ignore_col1)

df5 = df2[df3 & df4]
common_elements = df5['Column']
df1.drop(common_elements, axis = 1, inplace = True)
#print(df1)


'''Find occurrences -  move this piece of code according to requirements
'''
updated_cols = df1.columns
print("New cols=", updated_cols)

df1['concat'] = pd.Series(df1.fillna('').values.tolist()).map(lambda x: '~'.join(map(str,x)))

df1['is_duplicated'] = df1.duplicated(updated_cols)
no_duplicated = df1['is_duplicated'].sum()
print("Number of duplicates = ", no_duplicated)

df1['duplicate_occurrences'] = df1.groupby(list(df1['concat'])).cumcount()+1
df1[df1.duplicated(subset=updated_cols, keep = 'first')]

#Write to Alteryx output
#Alteryx.write(df1, 1)
print(df1)