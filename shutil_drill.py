import shutil
import os


source = 'C:\\Users\\Student\\Desktop\\shutil\\Folder A\\'
dest1 = 'C:\\Users\\Student\\Desktop\\shutil\\Folder B\\'

def move(source,dest1):
    files = os.listdir(source)

    for f in files:
        if f.endswith(".txt"):
            shutil.move(source + f, dest1)
            print dest1 + f
move(source,dest1)
       
        
        
