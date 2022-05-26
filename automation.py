import os
from shutil import move

#os.getenv('USER') gets the users environment variable (in our example it is the username)
USER = os.getenv('USER')

#go to root directory where most files will be stored
root_dir = '/Users/{}/Downloads/'.format(USER)
#go to each root directory per file type:
image_dir = '/Users/{}/Downloads/images/'.format(USER)
documents_dir = '/Users/{}/Downloads/documents/'.format(USER)
others_dir = '/Users/{}/Downloads/others/'.format(USER)
software_dir = '/Users/{}/Downloads/softwares/'.format(USER)


#python has the move function which allows us to move files from one directory to another




type_of_files_dict = {'word': 'docx', 'excel': 'xlsx', 'powerpoint': 'pptx', 'pdf': 'pdf', 'image': 'jpg', 'video': 'mp4', 'audio': 'mp3', 'text': 'txt'}
#use dict comprehension if possible for more practice
#write function to find the file type, then use that to move the file to the correct folder
#we must take the downloads folder, access the files there, then move them to the correct folder using the folder's os path

def find_type(file):
    pass
