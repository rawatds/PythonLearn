import os
import pathlib

# Deleting files

file = "C:\\Dharmender\\Data\\PythonLearn\\mydir\\dir_a\\a1.txt"
#os.remove(file)

file = "C:\\Dharmender\\Data\\PythonLearn\\mydir\\dir_a\\a4.txt"
#os.unlink(file)

file = "C:\\Dharmender\\Data\\PythonLearn\\mydir\\dir_a\\a1.txt"
#pathlib.Path(file).unlink()


# Deleting directory : All throws --> PermissionError: [WinError 5] Access is denied: 'C:\\Dharmender\\Data\\PythonLearn\\mydir\\dir_a'
file = "C:\\Dharmender\\Data\\PythonLearn\\mydir\\dir_a"
#os.remove(file)

file = "C:\\Dharmender\\Data\\PythonLearn\\mydir\\dir_a"
#os.unlink(file)

file = "C:\\Dharmender\\Data\\PythonLearn\\mydir\\dir_a"
#pathlib.Path(file).unlink()


# Deleting non-empty directory : these 2 will throw --> OSError: [WinError 145] The directory is not empty: 'C:\\Dharmender\\Data\\PythonLearn\\mydir\\dir_a'
file = "C:\\Dharmender\\Data\\PythonLearn\\mydir\\dir_a"
#os.rmdir(file)

file = "C:\\Dharmender\\Data\\PythonLearn\\mydir\\dir_a"
#pathlib.Path(file).rmdir()


# Deleting entiry directory tree
import shutil
file = "C:/Dharmender/Data/PythonLearn/mydir/dir_a/dir_a1"

shutil.rmtree(file)




