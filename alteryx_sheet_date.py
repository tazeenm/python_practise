'''
Python script that reads a parameter file and renames the files according to the given format (Date_SheetName or SheetName_Date)
Can add more date formats in config.xlsx (No code is touched)
'''
#Alteryx.installPackages("PackageName")
import pandas as pd
import xlrd 
from xlrd import open_workbook
import datetime

class SheetRenameWithDate:
    def readFiles(self):
        #df1 = Alteryx.read("#1")
        input_file = r'C:\Users\Tazeen.Munnavar\OneDrive\Documents\Python\Files\PROD_LNG_Portfolio_PNL.xlsx'
        xlsx = pd.ExcelFile(input_file)
        df1 = pd.read_excel(xlsx, 'Sheet1')
        
        #Config File Path with date formats
        date_file = open_workbook(r'C:\Users\Tazeen.Munnavar\OneDrive\Documents\Python\Files\config.xlsx')
        xl_sheet = date_file.sheet_by_index(0)
        return df1, xl_sheet

    def splitDataFrames(self, df1, xl_sheet):
        date_dict = {}
        for i in range(1, xl_sheet.nrows):
            row = xl_sheet.row_values(i)
            date_dict[row[0]] = row[1]
        print("Dictionary", date_dict)

        #Get's today's date
        date =  datetime.datetime.today().strftime('%Y-%m-%d')
        date1 = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        print("DATE", date1)
        print("Given Sheet name format\n", df1['SheetNameFormat'])

        df1['SheetNameFormat_Split1'] = df1['SheetNameFormat'].str.partition('_')[0]
        print("Split1\n", df1['SheetNameFormat_Split1'])

        df1['SheetNameFormat_Split2'] = df1['SheetNameFormat'].str.partition('_')[2]
        print("Split2\n", df1['SheetNameFormat_Split2'])
        return date1, date_dict 

    def changeDateFormat(self, date1, date_dict):
        sheet_format_list1 = df1['SheetNameFormat_Split1'].tolist()
        condition1 = any(key in date_dict for key in sheet_format_list1)
        if(condition1):
            print("Date format in Split 1")
            given_format = df1['SheetNameFormat_Split1'].str.extract('([a-zA-Z ]+)', expand = False)
            given_format = given_format.iloc[0]
            #given_format = given_format.to_string()
            print("Required Format: ", given_format)
        else:
            print("Sheet in split 1")
            given_format = df1['SheetNameFormat_Split2'].str.extract('([a-zA-Z ]+)', expand = False)
            given_format = given_format.iloc[0]
            #given_format = given_format.to_string()
            print("Required Format: ", given_format)

        value = date_dict.get(given_format)
        print("Format to be used: ", value)

        new_date = datetime.date.strftime(date1, value)
        print("Formatted Date: ", new_date)
        print(df1)
        return new_date, sheet_format_list1


    def renameSheet(self, new_date, date_dict, sheet_format_list1):
        #sheet_names_list = df1['SheetName'].tolist()
        #print("List", sheet_names_list)

        condition2 = any(key in date_dict for key in sheet_format_list1)
        if(condition2):
            x = df1['SheetName'].iteritems()
            for sheet in x:
                sheet_name = ''.join(sheet[1])
                #Renamed output Date_SheetName - Alteryx.write(df1, 1)
                renamed_sheet = new_date + '_' + sheet_name
                print(renamed_sheet)
            print("DATE")
        else:
            y = df1['SheetName'].iteritems()
            for sheet in y:
                sheet_name = ''.join(sheet[1])
                #Renamed output SheetName_Date - Alteryx.write(df1, 1)
                renamed_sheet = sheet_name + '_' + new_date
                print(renamed_sheet)
            print("SHEET")
        return renamed_sheet

if __name__ == "__main__":
    obj = SheetRenameWithDate()
    df1, xl_sheet = obj.readFiles()
    date1, date_dict = obj.splitDataFrames(df1, xl_sheet)
    new_date, sheet_format_list1 = obj.changeDateFormat(date1, date_dict)
    renamed_sheet = obj.renameSheet(new_date, date_dict, sheet_format_list1)
    



