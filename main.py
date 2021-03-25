#%% 
import os
import getpass

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
    while(dir_loc == ""):
        dir_loc = input('Input directory for files/folders compression/uncompression:')
        if(dir_loc == ""):
             print('No input detected. Directory cannot be found.')
        else:
            files = []
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
    password_protect = ""
    while(password_protect == ""):
        password_protect = str.lower(input('password protect all files and folders (y/n)? '))
        if(password_protect == "y" or password_protect == "n"):
            break
        else:
            print('Input must be either "y" or "n"')
            password_protect = ""


# %%
