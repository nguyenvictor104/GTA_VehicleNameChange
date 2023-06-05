
# Import libraries
import os

# Insert the directory path in here
path = os.getcwd()
 

 
# Get the list of all files and directories
dir_list = os.listdir(path)

newName = input ("Enter new name (do not include extension): ")
 
for selectedFile in dir_list:
    
    split_tup = os.path.splitext(selectedFile)

    # extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]
    if file_extension == (".xml"):
        if '_' in file_name:       
            newVehName = (newName+"_hi"+file_extension)
            os.rename(selectedFile,newVehName)
        else:
            newVehName = (newName+file_extension)
            os.rename(selectedFile,newVehName)
    if file_extension == (".yft"):
        if '_' in file_name:       
            newVehName = (newName+"_hi"+file_extension)
            os.rename(selectedFile,newVehName)
        else:
            newVehName = (newName+file_extension)
            os.rename(selectedFile,newVehName)
    if file_extension == (".ytd"):
        if '_' in file_name:       
            newVehName = (newName+"_hi"+file_extension)
            os.rename(selectedFile,newVehName)
        else:
            newVehName = (newName+file_extension)
            os.rename(selectedFile,newVehName)
        
 
