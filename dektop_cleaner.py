import os
import shutil 
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

#add any extenstions you'd like to the dictionary, make sure to also add coresponding code to getType
extensions = {"pdfs": '.pdf', "shortcuts":'.lnk', "docs":'.docx', "pictures": '.png', "texts": '.txt'}
    

def getType (filename):
    if (filename.endswith(extensions["pdfs"]) or filename.endswith(extensions["pdfs"].upper())):
        return extensions["pdfs"]
    elif (filename.endswith(extensions["shortcuts"]) or filename.endswith(extensions["shortcuts"].upper())):
        return extensions["shortcuts"]
    elif (filename.endswith(extensions["docs"]) or filename.endswith(extensions["docs"].upper())):
        return extensions["docs"]
    elif (filename.endswith(extensions["pictures"]) or filename.endswith(extensions["pictures"].upper())):
        return extensions["pictures"]
    elif (filename.endswith(extensions["texts"]) or filename.endswith(extensions["texts"].upper())):
        return extensions["texts"]
    else:
        return 'other'
    
def getFolderName (extension):
    for key, val in extensions.items():
        if (val == extension):
            return key
        
def moveFiles (folder_Path, file_path):
    
    if (not os.path.exists(folder_Path)):
        os.mkdir(folder_Path)
    
    shutil.move(file_path, folder_Path)

def moveFolders (file_path, folder_Path):
    shutil.move(file_path, folder_Path)

#Main function starts below
    
# Iterate through files on the desktop
for filename in os.listdir(desktop_path):

    extension = getType(filename)
    file_path = os.path.join(desktop_path, filename)

    if (os.path.isfile(file_path)):
        if (extension == 'other'):
            folder_path = os.path.join(desktop_path, 'others')
            moveFiles(folder_path,  file_path)
        else:
            folder_path = os.path.join(desktop_path, getFolderName(extension))
            moveFiles(folder_path,  file_path)
    elif (os.path.isdir(file_path)):
        folder_path = os.path.join(desktop_path, 'folders')
        if (not os.path.exists(folder_path)):
            os.mkdir(folder_path)
        moveFolders(file_path, folder_path)