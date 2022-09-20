import shutil
import os

def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)
            # print(filename)

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    name = list(filename.replace(' ', '_').split('.')[0])
    suffix = filename.split('.')[1].lower()
    for i in range(len(name) - 1):
        if name[i].islower() == True and name[i + 1].isupper() == True:
            name[i + 1] = '_' + name[i + 1]
    new_name = "".join(name)+ '.' + suffix
    return new_name


main()