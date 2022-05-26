import os #allows us to interact with the directory
from shutil import move #offers high level file interaction

#os.getenv('USER') gets the users environment variable (in our example it is the username)
USER = os.getenv('USER')

#go to root directory where most files will be stored
root_dir = '/Users/{}/Downloads/'.format(USER)
#go to each root directory per file type:
img_dir = '/Users/{}/Downloads/images/'.format(USER)
documents_dir = '/Users/{}/Downloads/documents/'.format(USER)
others_dir = '/Users/{}/Downloads/others/'.format(USER)
software_dir = '/Users/{}/Downloads/softwares/'.format(USER)

#possible file types:
document_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff', '.bmp')
software_types = ('.exe', '.pkg', '.dmg', '.msi', '.app', '.deb', '.rpm', '.msp')


#grab all files in root directory excluding current file
def get_files(root_dir):
    return [f for f in os.listdir(root_dir) if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]

#to move files to thier proper directory using the 'move(item, destination)' function, THIS WILL OVERRIDE FILES IF THEY EXIST
def move_files(files):
    for file in files: #itteratig through the list with all our files
        if file.endswith(document_types):
            if file not in documents_dir:
                move(file, documents_dir)
            #move(file, '{}/{}'.format(documents_dir, file))
        elif file.endswith(img_types):
            if file not in img_dir:
                move(file, img_dir)
            #move(file, '{}/{}'.format(img_dir, file))
        elif file.endswith(software_types):
            if file not in software_dir:
                move(file, software_dir)
            #move(file, '{}/{}'.format(software_dir, file))
        else:
            if file not in others_dir:
                move(file, others_dir)
            #move(file, '{}/{}'.format(others_dir, file))

if __name__ == '__main__':
    files = get_files(root_dir)
    move_files(files)