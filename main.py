#%% 
import os
import getpass
import re

#%%
project_description = "Compress each top level directory(s) and/or file(s) listed at a specific path location into seperate compressed files without needing to use 7zip commands for each individual item. You will only need to provide one password for a collection of items."
print(project_description)

# %%
system_process = os.system('7z')
if(system_process == 32512):
    print('7z cli tools not installed')
    input('Press enter to end program.')
else:
    compress = ""
    while(compress == ""):
        compress = str.lower(input('Compress or uncompress all (compress/uncompress): '))
        if(compress == "compress" or compress == "uncompress"):
           break
        else:
            print('Input must be either "compress" or "uncompress"')
            compress = ""
# %%

    dir_loc = ""
    files = []
    while(dir_loc == ""):
        dir_loc = input('Input directory for files/folders compression/uncompression:')
        if(dir_loc == ""):
             print('No input detected. Directory cannot be found.')
        else:
            try:
                files = os.listdir(dir_loc)
                if(len(files) == 0):
                    print('Directory does not contain any files or folders')
                    dir_loc = ""
                else:
                    break
            except FileNotFoundError:
                dir_loc = ""
                print('Directory does not exist')

            
# %%

    os.system(f'cd {dir_loc}')


# %%
    password_protect = ""
    password = "" 
    while(password_protect == ""):
        password_protect = str.lower(input('password protect all files and folders (y/n)? '))
        if(password_protect == "y" or password_protect == "n"): 
            if(password_protect == "y"):
                while(password == ""):
                    password = getpass.getpass("Password: ")
                    if(len(password) < 10):
                        print('Length of password must be greater than 10 characters')        
                    if(re.search(r"\d", password ) == None):
                        print('Password must contain at least one digit')
                    if(re.search(r"[!@#$%^&*:<?]", password) == None):
                        print('Password must contain at least one of the following special characters !@#$%^&*:<?')

                    password_verify = getpass.getpass("Verify Password: ")
                    if(password != password_verify):
                        print("Password does not match, try again.")
                        password = ""
                    else:
                        break
            else:
                break
        else:
            print('Input must be either "y" or "n"')
            password_protect = ""

# %%
for file in files:
    print(file)

# %%
