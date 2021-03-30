import cmd
from pathfinder import Pathfinder
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
        if line[:4] == 'help':
            return line
        try:
            args = args[0] + ' ' + ' '.join(map(self.pathfinder.make_path, args[1:]))
        except EnvironmentError:
            return 'oos'
        else:
            return args

    def do_oos(self, arg):
        print('Access denied!')

    def do_pwd(self, arg):
        'Print working directory: pwd'
        print(self.pathfinder.working_directory)

    def do_lsd(self, arg):
        'List of all files and directories in current direction:\n\tlsd'
        print('\n'.join(list_dir(self.pathfinder.working_directory)))

    def do_chd(self, destination):
        'Change working directory:\n\tchd myDir'
        print(self.pathfinder.change_wd(destination))

    def do_crd(self, name):
        'Create a new directory:\n\tcrd myDir'
        print(create_dir(name))

    def do_rmd(self, name):
        'Remove a directory:\n\trmd myDir'
        print(remove_dir(name))

    def do_crf(self, name):
        'Create a new file:\n\tcrf myFile'
        print(create_file(name))

    def do_rmf(self, name):
        'Remove a file:\n\trmf myFile'
        print(remove_file(name))

    def do_wtf(self, arg):
        'Write to file:\n\twtf myFile'
        print(write_to_file(arg))

    def do_rdf(self, arg):
        'Read a file:\n\trdf myFile'
        print(read_file(arg))

    def do_cpf(self, args):
        'Copy a file: cpf srcFile destFile'
        print(copy_file(*args.split(' ')))

    def do_mvf(self, args):
        'Move a file: mvf srcFile destFile'
        print(move_file(*args.split(' ')))

    def do_exit(self, arg):
        'Exit file manager: exit'
        print('Thank you for using Fima')
        return True
