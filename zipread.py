import zipfile
import os

# Creting a zip
files = ["mydir/file1.txt", "mydir/file4.txt", "mydir/dir_b/b1.txt" ,"assert.py"]
with zipfile.ZipFile("mydir.zip", "w") as zfile:
    for file in files:
        zfile.write(file)



# Reading a zip
with zipfile.ZipFile("mydir.zip", "r") as zfile:
    #print(zipfile.namelist())
    for file in zfile.namelist():
        finfo = zfile.getinfo(file)
        print(finfo.filename, ":", finfo.file_size, " / ", finfo.compress_size, ", ", finfo.compress_type, ", ", finfo.date_time)

#os.listdir('c:/tmp')

# Extra the zip
#fzip = zipfile.ZipFile("mydir.zip", "r")
zfile = zipfile.ZipFile("mydir.zip", "r")
zfile.extractall("c:/tmp/dd")
zfile.close()

