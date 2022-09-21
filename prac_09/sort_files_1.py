import os
import shutil

def move_files():
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            try:
                extension = filename.split('.')[1]
                shutil.move(filename, extension)
            except shutil.Error:
                continue

def create_folders(extended_list):
    for extension in extended_list:
        try:
            os.mkdir(extension)
        except FileExistsError:
            continue

def get_extended_list():
    extension_list = []
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            extension = filename.split('.')[1]
            if extension not in extension_list:
                extension_list.append(extension)
    return extension_list

def main():
    os.chdir('FilesToSort')
    extended_list = get_extended_list()
    create_folders(extended_list)
    move_files()

main()