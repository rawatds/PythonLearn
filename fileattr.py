import pathlib, os
from datetime import datetime



def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y %T')
    return formatted_date



basepath = 'mydir'

print("======= Listing file attributes ==================")
for entry in pathlib.Path(basepath).iterdir():
        info = entry.stat()
        print("%-20s" % (entry.name), "Created: ", convert_date(info.st_ctime), ', Accessed: ',  convert_date(info.st_atime), ', Modified: ',  convert_date(info.st_mtime), sep='')

