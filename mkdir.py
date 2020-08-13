import pathlib, os

dir = "mydir"

# Single directory
# os.mkdir(dir)                 # FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'mydir'
# pathlib.Path(dir).mkdir()     # FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'mydir'

pathlib.Path(dir).mkdir(exist_ok=True)

os.makedirs("2020/07/30", exist_ok=True)     #
 

pathlib.Path("2010/01/04").mkdir(exist_ok=True, parents=True, mode=0o744)