import datetime  # to write to current time to log file
import os  # allows us to interact with the directory
from shutil import move  # offers high level file interaction

#
# def mkdirs(typeOf):
#     if not os.path.isdir(currDir + "/{}".format(typeOf)):
#         os.mkdir("{}".format(typeOf))

curr_dir = str(os.getcwd())
logFile = open(curr_dir + "/log.txt", "a")


# take in a list of all the files from the current directory
# fileTypes is all the types of that file i.e for img -> .png, .jpeg etc...
def relocate_files_by_type(files) -> list[str]:
    file_types = {'document_types': '.doc .docx .txt .pdf .xls .ppt .xlsx .pptx .zip',
                  'img_types': '.JPG .jpeg .png .svg .gif .tif .tiff .bmp .psd .HEIC',
                  'software_types': '.exe .pkg .dmg .msi .app .deb .rpm .msp .iso',
                  'code_types': '.py .java .html .js .jsx'
                  }
    for idx, file in enumerate(files):
        # grab the file extension by splitting on the dot
        file_extension = file.split('.')[-1]
        # dog.png -> file_extension = png

        #get a way to figure out which folder its supposed to go to, currently wont do anything if the files extension != directory name
        if file_extension and file not in str(curr_dir + file_extension + "/"):
            try:
                move(file, curr_dir + file_extension + "/")
                logFile.write('Successfully moved {} to {} folder on {}\n'.format(file, file_extension, datetime.datetime.now()))
                del files[idx]
            except Exception as e:
                if isinstance(e, FileExistsError):
                    move(file, curr_dir + "/failed/")
                    print("failed to move {}, File already Existed, moving to failed directory".format(file))
                logFile.write("Failed to move file {} -> {} on {}\n".format(file, e, datetime.datetime.now()))

    return files
