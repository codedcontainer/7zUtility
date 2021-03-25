import os
import subprocess
import getpass
import re

class FileCompression7z:
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
    compress = ""
    dir_loc = ""
    files = []
    password_protect = ""
    password = "" 

    def __init__(self):
        self.print_description()
        self.check7z()
        self.compression_prompt()
        self.parent_directory_prompt()
        self.password_protection_prompts()
        self.file_compression_actions()        

    def print_description(self):
        print(self.project_description)

    def check7z(self):
        try:
            subprocess.check_output('7z')
        except OSError:
            print('7z cli tools not installed')
            input('Press enter to end program: ')
            exit()


    def compression_prompt(self):
        while(self.compress == ""):
            self.compress = str.lower(input('Compress or uncompress all (compress/uncompress): '))
            if(self.compress == "compress" or self.compress == "uncompress"):
                break
            else:
                print('Input must be either "compress" or "uncompress"')
                self.compress = ""


    def parent_directory_prompt(self):
        while(self.dir_loc == ""):
            self.dir_loc = input('Parent target directory of file(s)/folder(s):')
            self.dir_loc = self.dir_loc.strip("\"")

            if(self.dir_loc == ""):
                    print('Target directory cannot be found.')
            else:
                try:
                    self.files = os.listdir(self.dir_loc)
                    if(len(self.files) == 0):
                        print('Target directory does not contain any files or folders')
                        self.dir_loc = ""
                    else:
                        break
                except FileNotFoundError:
                    self.dir_loc = ""
                    print('Taget directory does not exist')


    def password_protection_prompts(self): 
        while(self.password_protect == ""):
            self.password_protect = str.lower(input('Password protection for all files and folders (y/n)? '))
            if(self.password_protect == "y" or self.password_protect == "n"): 
                if(self.password_protect == "y"):           
                    while(self.password == ""):
                        if(self.compress == "compress"):
                            print("Password must be greater than 10 characters, contain at least one digit, and have at least one of the following characters: !@#$%^&*:<?")
                        
                        self.password = getpass.getpass("Password (no echo): ")
                        if(self.compress == "compress"):                    
                            if(len(self.password) < 10):
                                print('Length of password must be greater than 10 characters')
                                self.password = ""        
                            if(re.search(r"\d", self.password ) == None):
                                print('Password must contain at least one digit')
                                self.password = ""
                            if(re.search(r"[!@#$%^&*:<?]", self.password) == None):
                                print('Password must contain at least one of the following special characters !@#$%^&*:<?')
                                self.password = ""                

                        if(self.password != ""):                                  
                            password_verify = getpass.getpass("Verify Password (no echo): ")
                            if(self.password != password_verify):
                                print("Password does not match, try again.")
                                self.password = ""
                else:
                    break
            else:
                print('Input must be either "y" or "n"')
                self.password_protect = ""


    def file_compression_actions(self):
        for file in self.files:
            if(self.compress == "compress"):
                file = file.replace(" ", "-")
                if(re.search('[.]', file) == None):
                    if(self.password != ""):
                        os.system(f"cd {self.dir_loc} && 7z a -p'{self.password}' {file}-encrypted.7z '{file}'")
                    else:
                        os.system(f"cd {self.dir_loc} && 7z a {file}-encrypted.7z '{file}'")
                else:
                    file_no_extension = file.split(',')[0]
                    print(file_no_extension)
                    if(self.password != ""):
                        os.system(f"cd {self.dir_loc} && 7z a -p'{self.password}' {file_no_extension}-encrypted.7z '{file}'")
                    else:
                        os.system(f"cd {self.dir_loc} && 7z a {file_no_extension}-encrypted.7z '{file}'")
            else:
                if ".7z" in file:
                    if(self.password != ""):
                        os.system(f"cd {self.dir_loc} && 7z x -y -p'{self.password}' '{file}'")
                    else:
                        os.system(f"cd {self.dir_loc} && 7z x -y '{file}'")


FileCompression7z()
