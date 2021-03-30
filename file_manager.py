import cmd
from pathfinder import Pathfinder
import os
from commands import *


class FileManager(cmd.Cmd):
    def __init__(self):
        super().__init__()
        with open('cfg.txt') as f:
            root = f.readline()
        self.pathfinder = Pathfinder(root)

    intro = 'Welcome to Fima file manager.   Type help or ? to list commands.\n'
    prompt = '(Fima) '

    def precmd(self, line):
        args = line.split(' ')
        try:
            args = args[0] + ' ' + ' '.join(map(self.pathfinder.make_path, args[1:]))
        except EnvironmentError:
            return 'oos'
        else:
            return args

    def do_oos(self, arg):
        print('Access denied!')

    def do_pwd(self, arg):
        print(self.pathfinder.working_directory)

    def do_lsd(self, arg):
        'List of all files and directories in current direction: lsd'
        print('\n'.join(list_dir(self.pathfinder.working_directory)))

    def do_chd(self, destination):
        'Change working directory: chd myDir'
        print(self.pathfinder.change_wd(destination))

    def do_crd(self, name):
        'Create a new directory: crd myDir'
        print(create_dir(name))

    def do_rmd(self, name):
        'Remove a directory: rmd myDir'
        print(remove_dir(name))

    def do_crf(self, name):
        'Create a new file: crf myFile'
        print(create_file(name))

    def do_rmf(self, name):
        'Remove a file: rmf myFile'
        print(remove_file(name))

    def do_rdf(self, arg):
        'Read a file: rdf myFile'
        print(read_file(arg))

    def do_cpf(self, args):
        print(copy_file(*args.split(' ')))

    def do_mvf(self, args):
        print(move_file(*args.split(' ')))

    def do_exit(self, arg):
        'Exit file manager: exit'
        print('Thank you for using Fima')
        return True
