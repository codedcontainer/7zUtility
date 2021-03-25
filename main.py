import os
import subprocess
import getpass
import re

project_description = """
*****************************************************************
|          Python 7z File Compression Utility Program           |
*****************************************************************
| Compress or uncompress each top level directory(s)            | 
| and/or file(s) listed at a specific path location into        | 
| seperate compressed files without needing to use 7zip         |
| commands for each individual item. You will only need to      | 
| provide one password for a collection of items.               |
*****************************************************************
"""
print(project_description)

def check7z():
    try:
        subprocess.check_output('7z')
    except OSError:
        print('7z cli tools not installed')
        input('Press enter to end program: ')
        exit()


def compression_prompt():
    compress = ""
    while(compress == ""):
        compress = str.lower(input('Compress or uncompress all (compress/uncompress): '))
        if(compress == "compress" or compress == "uncompress"):
            break
        else:
            print('Input must be either "compress" or "uncompress"')
            compress = ""


def parent_directory_prompt():
    dir_loc = ""
    files = []
    while(dir_loc == ""):
        dir_loc = input('Parent target directory of file(s)/folder(s):')
        if(dir_loc == ""):
                print('Target directory cannot be found.')
        else:
            try:
                files = os.listdir(dir_loc)
                if(len(files) == 0):
                    print('Target directory does not contain any files or folders')
                    dir_loc = ""
                else:
                    break
            except FileNotFoundError:
                dir_loc = ""
                print('Taget directory does not exist')


def password_protection_prompts():
    password_protect = ""
    password = "" 
    while(password_protect == ""):
        password_protect = str.lower(input('Password protection for all files and folders (y/n)? '))
        if(password_protect == "y" or password_protect == "n"): 
            if(password_protect == "y"):           
                while(password == ""):
                    if(compress == "compress"):
                        print("Password must be greater than 10 characters, contain at least one digit, and have at least one of the following characters: !@#$%^&*:<?")
                    
                    password = getpass.getpass("Password (no echo): ")
                    if(compress == "compress"):                    
                        if(len(password) < 10):
                            print('Length of password must be greater than 10 characters')
                            password = ""        
                        if(re.search(r"\d", password ) == None):
                            print('Password must contain at least one digit')
                            password = ""
                        if(re.search(r"[!@#$%^&*:<?]", password) == None):
                            print('Password must contain at least one of the following special characters !@#$%^&*:<?')
                            password = ""                

                    if(password != ""):                                  
                        password_verify = getpass.getpass("Verify Password (no echo): ")
                        if(password != password_verify):
                            print("Password does not match, try again.")
                            password = ""
            else:
                break
        else:
            print('Input must be either "y" or "n"')
        password_protect = ""


def file_compression_actions():
    for file in files:
        if(compress == "compress"):
            file = file.replace(" ", "-")
            if(re.search('[.]', file) == None):
                if(password != ""):
                    os.system(f"cd {dir_loc} && 7z a -p'{password}' {file}-encrypted.7z '{file}'")
                else:
                    os.system(f"cd {dir_loc} && 7z a {file}-encrypted.7z '{file}'")
            else:
                file_no_extension = file.split(',')[0]
                print(file_no_extension)
                if(password != ""):
                    os.system(f"cd {dir_loc} && 7z a -p'{password}' {file_no_extension}-encrypted.7z '{file}'")
                else:
                    os.system(f"cd {dir_loc} && 7z a {file_no_extension}-encrypted.7z '{file}'")
        else:
            if ".7z" in file:
                if(password != ""):
                    os.system(f"cd {dir_loc} && 7z x -y -p'{password}' '{file}'")
                else:
                    os.system(f"cd {dir_loc} && 7z x -y '{file}'")


check7z()
compression_prompt()
parent_directory_prompt()
password_protection_prompts()
file_compression_actions()
