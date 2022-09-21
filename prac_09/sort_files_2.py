import os
import shutil

def move_files(category_to_extensions):
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            try:
                extension = filename.split('.')[1]
                for category, extensions in category_to_extensions.items():
                    if extension in extensions:
                        shutil.move(filename, category)
            except shutil.Error:
                continue

def create_folder(category_to_extensions):
    for category in category_to_extensions:
        try:
            os.mkdir(category)
        except FileExistsError:
            continue

def main():
    os.chdir('FilesToSort')
    extensions_list = []
    category_to_extensions = {}
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            extension = filename.split('.')[1]
            if extension not in extensions_list:
                extensions_list.append(extension)
    for extension in extensions_list:
        choice = input("What category would you like to sort {} files into? ".format(extension))
        if choice in category_to_extensions:
            category_to_extensions[choice].append(extension)
        else:
            category_to_extensions[choice] = [extension]
    create_folder(category_to_extensions)
    move_files(category_to_extensions)

main()