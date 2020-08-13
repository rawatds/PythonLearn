from tempfile import TemporaryFile, TemporaryDirectory
import time, os


fp = TemporaryFile("w+t")
fp.write("Hello world!")

print(fp.name)

time.sleep(10)

fp.seek(0)
data = fp.read()

print("From file: ", data)

fp.close()

print("Temporary file deleted")

with TemporaryDirectory() as fp:
    print(fp)
    time.sleep(10)
    print(os.path.exists(fp))

print("Done")



