import os #allows us to interact with the directory
import sys #allow the usage of argv cmmd
from shutil import move #offers high level file interaction
import datetime #to write to current time to log file

#all possible file types:
document_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff', '.bmp')
software_types = ('.exe', '.pkg', '.dmg', '.msi', '.app', '.deb', '.rpm', '.msp')

#current working dir
currDir = str(os.getcwd())

files = [f for f in os.listdir(".") if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]

logFile = open(currDir+"/log.txt","a")

if not os.path.isdir(currDir+"/failed"):
    os.mkdir("failed")

if os.path.isdir(currDir+"/img"):
    for idx,file in enumerate(files):
        if file.endswith(img_types) and file not in currDir+"img/":
            try:
                move(file, currDir+"/img/")
                logFile.write('Successfully moved {} to img folder on {}\n'.format(file, datetime.datetime.now()))
                del files[idx]
            except Exception as e:
                if isinstance(e, FileExistsError):
                    print("similar error")
                    move(file, currDir+"/failed/")
                    print("failed to move {}, File already Existed, moving to failed directory".format(file))
                logFile.write("Failed to move file {}, because {}\n".format(file,e))
else:
    os.mkdir("img")

if os.path.isdir(currDir+"/docs"):
    for idx,file in enumerate(files):
        if file.endswith(document_types) and file not in currDir+"docs/" and file != "log.txt":
            try:
                move(file, currDir+"/docs/")
                logFile.write('Successfully moved {} to docs folder on {}\n'.format(file, datetime.datetime.now()))
                del files[idx]
            except Exception as e:
                if isinstance(e, FileExistsError):
                    move(file,currDir+"/failed/")
                    print("failed to move {}, File already Existed, moving to failed directory".format(file))
                logFile.write("Failed to move file {}, because {}\n".format(file,e))
else:
    os.mkdir("docs")

if os.path.isdir(currDir+"/software"):
    for idx,file in enumerate(files):
        if file.endswith(software_types) and file not in currDir+"software/":
            try:
                move(file, currDir+"/software/")
                logFile.write('Successfully moved {} to software folder on {}\n'.format(file, datetime.datetime.now()))
                del files[idx]
            except Exception as e:
                if isinstance(e, FileExistsError):
                    move(file,currDir+"/failed/")
                    print("failed to move {}, File already Existed, moving to failed directory".format(file))
                logFile.write("Failed to move file {}, because {}\n".format(file,e))
else:
    os.mkdir("software")

# if os.path.isdir(currDir+"/other"):
#     for idx,file in enumerate(files):
#         if file not in currDir+"other/":
#             try:
#                 move(file, currDir+"/other/")
#                 logFile.write('Successfully moved {} to other folder on {}\n'.format(file, datetime.datetime.now()))
#             except Exception as e:
#                 if isinstance(e, FileExistsError):
#                     move(file,currDir+"/failed/")
#                     print("failed to move {}, File already Existed, moving to failed directory".format(file))
#                 logFile.write("Failed to move file {}, because {}\n".format(file,e))
# else:
#     os.mkdir("other")

logFile.close()

def main():
    if __name__ == '__main__':
        print("-------->RUNNING PROGRAM<--------")
main()