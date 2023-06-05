
# Import libraries
import os

# Insert the directory path in here
path = os.getcwd()
 

 
# Get the list of all files and directories
dir_list = os.listdir(path)
 
for selectedFile in dir_list:
    split_tup = os.path.splitext(selectedFile)
    # extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]
    if file_extension == (".xml"):
        print (selectedFile)
        os.remove(selectedFile)
    if file_extension == (".yft"):
        print (selectedFile)
        os.remove(selectedFile)
    if file_extension == (".ytd"):
        print (selectedFile)
        os.remove(selectedFile)
        
