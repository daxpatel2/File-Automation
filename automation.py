import os #allows us to interact with the directory
import sys #allow the usage of argv cmmd
from shutil import move #offers high level file interaction
import datetime #to write to current time to log file

#we need better logging functionality so the user can check log file for all movements of files
log_open = open('/Users/daxpatel/Downloads/Log/log.txt', 'a')
log = log_open.write('File was read on {}\n'.format(datetime.datetime.now()))

filers = open('/Users/daxpatel/Downloads/Log/file_log.txt', 'a')
file_write = filers

#os.getenv('USER') gets the users environment variable (in our example it is the username so we can acess folders like \user\daxpatel\downloads)
USER = os.getenv('USER')

#directories that we want to clean
root_dir = '/Users/{}/Downloads/'.format(USER)
desktop_dir = '/Users/{}/Desktop/'.format(USER)

#go to each downloads directory per file type:
img_dir_downloads = '/Users/{}/Downloads/images/'.format(USER)
documents_dir_downloads = '/Users/{}/Downloads/documents/'.format(USER)
others_dir_downloads = '/Users/{}/Downloads/others/'.format(USER)
software_dir_downloads = '/Users/{}/Downloads/softwares/'.format(USER)
#go to each Desktop directory per file type:
desktop_img_dir = '/Users/{}/Desktop/images/'.format(USER)
desktop_documents_dir = '/Users/{}/Desktop/documents/'.format(USER)
desktop_others_dir = '/Users/{}/Desktop/others/'.format(USER)
desktop_software_dir = '/Users/{}/Desktop/softwares/'.format(USER)

#all possible file types:
document_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff', '.bmp')
software_types = ('.exe', '.pkg', '.dmg', '.msi', '.app', '.deb', '.rpm', '.msp')

#grab all files in specifeid directory using argv
argv = sys.argv[1]
if argv == 'downloads':
    go_dir = root_dir
elif argv == 'desktop':
    go_dir = desktop_dir

#specify the directory to search for files and grab a list of all the files in that directory
def get_files(go_dir):
    return [f for f in os.listdir(go_dir) if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]

files = get_files(go_dir)
#to move files to thier proper directory using the 'move(item, destination)' function, THIS WILL OVERRIDE FILES IF THEY EXIST
def move_files(files):
    for file in files: #itteratng through the list with all our files
        if file.endswith(document_types):
            if file not in go_dir+'documents/':
                try:
                    move(file, go_dir+'documents/')
                    file_write.write('Successfully moved {} to Documents folder on {}\n'.format(file, datetime.datetime.now()))
                except:
                    file_write.write('Failed to move {} to Documents folder\n'.format(file))
                    #write to the log file in caps for errors

        elif file.endswith(img_types):
            if file not in go_dir+'images/':
                try:
                    move(file, go_dir+'images/')
                    file_write.write('Successfully moved {} to Images folder on {}\n'.format(file, datetime.datetime.now()))
                except:
                    file_write.write('Failed to move {} to Images folder\n'.format(file))

        elif file.endswith(software_types):
            if file not in go_dir+'softwares/':
                try:
                    move(file, go_dir+'softwares/')
                    file_write.write('Successfully moved {} to Softwares folder {}\n'.format(file,datetime.datetime.now()))
                except:
                    file_write.write('Failed to move {} to Softwares folder\n'.format(file))
        else:
            if file not in go_dir+'others/':
                try:
                    move(file, go_dir+'others/')
                    file_write.write('Successfully moved {} to Others folder on {}\n'.format(file, datetime.datetime.now()))
                except:
                    file_write.write('Failed to move {} to Others folder\n'.format(file))

#will have to fix this to move files to their proper directory
def main():
    if __name__ == '__main__':
        files = get_files(go_dir)
        move_files(files)

main()