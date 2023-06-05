
# Import libraries
import os

# Insert the directory path in here
path = os.getcwd()
 

 
# Get the list of all files and directories
dir_list = os.listdir(path)

newName = input ("Enter new name (do not include extension): ")
 
for i in dir_list:
    
    split_tup = os.path.splitext(i)

    # extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]
    if file_extension != (".py" or ".exe" or ".txt"):
        if '_' in file_name:       
            newVehName = (newName+"_hi"+file_extension)
            os.rename(i,newVehName)
        else:
            newVehName = (newName+file_extension)
            os.rename(i,newVehName)
        

 
