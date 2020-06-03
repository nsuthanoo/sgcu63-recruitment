import json

#// assumption: There's more folders in the subfolders

#Function to search for a file
def search(file_name, JSON_file):
    #Load the JSON file
    with open(JSON_file,'r') as Jfile:
        directory=json.loads(Jfile.read())
    result=[]
    #Iterate through all folders(In case there're more than one)
    for parent_folder in directory.keys():
        #Get the list of files in the folder
        files_list=directory[parent_folder]["_files"]
        #Add the directory to result if the file is in the folder
        if file_name in files_list:
            result.append("/"+parent_folder+"/"+file_name)
        #Go through all subfolders
        for sub_folder in directory[parent_folder].keys():
            if sub_folder != "_files":
                 #Get the list of files in the subfolder
                files_list=directory[parent_folder][sub_folder]["_files"]
                #Add the directory to result if the file is in the subfolder
                if file_name in files_list:
                    result.append("/"+parent_folder+"/"+sub_folder+"/"+file_name)
    #Print out the result
    print(result)


#State the JSON file to use
JSON_file="Prob#2 - File Search/file.json"
#State the name of the file to search for
file_to_search='file1'

search(file_to_search,JSON_file)

