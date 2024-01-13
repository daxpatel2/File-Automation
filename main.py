import os  # allows us to interact with the directory
from shutil import move  # offers high level file interaction
from constants import *
import datetime  # to write to current time to log file

def mkdirs(type_of):
    print(currDir)
    if not os.path.isdir(currDir + "/{}".format(type_of)):
        os.mkdir("{}".format(type_of))

# current working dir
currDir = str(os.getcwd())

files = [f for f in os.listdir(".") if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]
print("{} is of type {}".format(files[0], type(files[0])))

logFile = open(currDir + "/log.txt", "a")
errFile = open(currDir + "/errLog.txt","a")

mkdirs("img")
for idx, file in enumerate(files):
    if file.endswith(img_types) and file not in currDir + "img/":
        try:
            move(file, currDir + "/img/")
            logFile.write('Successfully moved {} to img folder on {}\n'.format(file, datetime.datetime.now()))
            del files[idx]
        except Exception as e:
            errFile.write("Failed to move file {}, because {} on {}\n".format(file,e,datetime.datetime.now()))

mkdirs("docs")
for idx, file in enumerate(files):
    if file.endswith(document_types) and file not in currDir + "docs/" and file != "log.txt":
        try:
            move(file, currDir + "/docs/")
            logFile.write('Successfully moved {} to docs folder on {}\n'.format(file, datetime.datetime.now()))
            del files[idx]
        except Exception as e:
            errFile.write("Failed to move file {}, because {} on {}\n".format(file,e,datetime.datetime.now()))

mkdirs("software")
for idx, file in enumerate(files):
    if file.endswith(software_types) and file not in currDir + "software/":
        try:
            move(file, currDir + "/software/")
            logFile.write('Successfully moved {} to software folder on {}\n'.format(file, datetime.datetime.now()))
            del files[idx]
        except Exception as e:
            errFile.write("Failed to move file {}, because {} on {}\n".format(file,e,datetime.datetime.now()))

mkdirs("code")
for idx, file in enumerate(files):
    if file.endswith(code_types) and file not in currDir + "code/":
        try:
            move(file, currDir + "/code/")
            logFile.write('Successfully moved {} to code folder on {}\n'.format(file, datetime.datetime.now()))
            del files[idx]
        except Exception as e:
            errFile.write("Failed to move file {}, because {} on {}\n".format(file,e,datetime.datetime.now()))

logFile.close()
errFile.close()

def main():
    if __name__ == '__main__':
        print("-------->RUNNING PROGRAM<--------")
main()