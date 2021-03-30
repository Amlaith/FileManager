import os
import shutil


def get_working_directory():
    return os.getcwd()


def list_dir(path):
    return os.listdir(path)


def change_dir(destination):
    try:
        os.chdir(destination)
    except Exception as e:
        return f'Unable to change directory:\n\t{e}'
    else:
        return f'Current working directory:\n\t{os.getcwd()}'


def create_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        return f'Failed Creation of the directory:\n\t{path}'
    else:
        return f'Successfully created the directory:\n\t{path}'


def remove_dir(path):
    try:
        shutil.rmtree(path)
    except OSError:
        return f'Failed deletion of the directory\n\t{path}'
    else:
        return f'Successfully deleted the directory\n\t{path}'


def create_file(path):
    try:
        open(path, "x")
    except FileExistsError:
        return f'File already exists:\n\t{path}'
    except FileNotFoundError:
        dir_path = "\\".join(path.split("\\")[:-1])
        return f'No such directory:\n\t{dir_path}'
    else:
        return f'Successfully created the file:\n\t{path}'


def remove_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        return f'File does not exist:\n\t{path}'
    except PermissionError as e:
        return f'Unable to remove:\n\t{e}'
    else:
        return f'Successfully removed the file:\n\t{path}'


def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f'File does not exist:\n\t{path}'


def copy_file(source_path, destination_path):
    try:
        shutil.copyfile(source_path, destination_path)
    except IOError as e:
        return f'Unable to copy:\n\t{e}'
    else:
        return f'Successfully copied the file:\n\t{source_path}\nto\n\t{destination_path}'


def move_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
    except IOError as e:
        return f'Unable to move:\n\t{e}'
    else:
        return f'Successfully moved the file:\n\t{source_path}\nto:\n\t{destination_path}'


def rename_file(source_path, destination_path):
    try:
        os.rename(source_path, destination_path)
    except Exception as e:
        return f'Unable to rename file:\n\t{e}'
    else:
        return f'Successfully renamed the file:\n\t{source_path}\nto:\n\t{destination_path}'

