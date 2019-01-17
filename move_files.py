'''
A Python Script to create directories and move files from another folder to this one based on the date.
'''

import os
import sys
import shutil   #Move
import datetime 
import ctypes   #Message Box
import time

#Today's date
date_time = datetime.date.today()
date = str(date_time)
print(date)

#Source and Destination Path - Windows Path
src = 'C:\\Users\\Tazeen.Munnavar\\OneDrive\\Documents\\Alteryx\\DataFiles\\OUPUT'
dest1 = 'C:\\Users\\Tazeen.Munnavar\\OneDrive\\Documents\\Alteryx\\DataFiles\\'
dest = dest1 + 'Output' + date
print(dest)

# Create a Directory if doesn't exist
def create_directory():
        dir_name = 'Output' + date
        dir_path = os.path.join(dest1, dir_name)
        if not os.path.exists(dir_path):
                os.mkdir(dir_path)
                print("Directory " , dir_name ,  " Created ")
        else:
                def Mbox(title, text, style):
                        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
                Mbox('Info', 'Directory Exists!', 0)

#Move files from Output folder to their respective new folders
def move_files():
        src_files = os.listdir(src)
        for files in src_files:
                if(date in files):
                        print(files)
                        copy_file = os.path.join(src, files)
                        if(os.path.isfile(copy_file)):
                                shutil.move(copy_file, dest)

if __name__ == "__main__":
    create_directory()
    time.sleep(.500)
    move_files()
    
