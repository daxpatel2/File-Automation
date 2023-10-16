import os #allows us to interact with the directory
import sys #allow the usage of argv cmmd
import datetime #to write to current time to log file
from shutil import move #offers high level file interaction


def mkdirs(typeOf):
    if not os.path.isdir(currDir+"/{}".format(typeOf)):
        os.mkdir("{}".format(typeOf))



#take in a list of all the files from the current directory
#fileTypes is all the types of that file i.e for img -> .png, .jpeg etc...
def relocateFilesBasedOnType(files,fileTypes):
    for idx,file in enumerate(files):
        if file.endswith(fileTypes) and file not in str(currDir+fileTypes+"/"):
            try:
                move(file, currDir+fileTypes+"/")
                logFile.write('Successfully moved {} to img folder on {}\n'.format(file, datetime.datetime.now()))
                del files[idx]
            except Exception as e:
                if isinstance(e, FileExistsError):
                    move(file, currDir+"/failed/")
                    print("failed to move {}, File already Existed, moving to failed directory".format(file))
                logFile.write("Failed to move file {} -> {} on {}\n".format(file,e,datetime.datetime.now()))
