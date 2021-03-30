import cmd
from pathfinder import Pathfinder
from commands import *


class FileManager(cmd.Cmd):
    def __init__(self):
        super().__init__()
        # Из cfg.txt считывается рабочая директория,
        # за пределы которой выйти будет нельзя
        with open('cfg.txt') as f:
            root = f.readline()
        # Создается объект, преобразующий ввод в полноценные пути
        # Он получает на вход рут, и вернет код ошибки, если его покинуть
        self.pathfinder = Pathfinder(root)

    # Приветствие при запуске
    intro = 'Welcome to Fima file manager.   Type help or ? to list commands.\n'
    # Приглашение к вводу
    prompt = '(Fima) '

    # Метод, предварительно обрабатывающий ввод
    def precmd(self, line):
        # Если ввод - это просьба о помощи, она просто передается дальше
        if line[:4] == 'help' or line[0] == '?':
            return line
        # Если другая команда - из аргументов делаются абсолютные пути
        # Таким образом проверяется, не пытается ли пользователь
        # выйти за границы своих возможностей
        args = line.split(' ')
        try:
            args = args[0] + ' ' + ' '.join(map(self.pathfinder.make_path, args[1:]))
        except EnvironmentError:
            # Когда pathfinder возвращает код ошибки, пользовательский ввод
            # превращается в команду, вызывающую сообщение о отсутствии прав доступа
            return 'oos'
        else:
            return args

    def do_oos(self, arg):
        'Punishes you for leaving a root tree'
        print('Access denied!')

    def do_pwd(self, arg):
        'Print working directory: pwd'
        print(self.pathfinder.working_directory)

    def do_lsd(self, arg):
        'List of all files and directories in current directory:\n\tlsd'
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
        'Copy a file:\n\tcpf srcFile destFile'
        print(copy_file(*args.split(' ')))

    def do_mvf(self, args):
        'Move a file:\n\tmvf srcFile destFile'
        print(move_file(*args.split(' ')))

    def do_exit(self, arg):
        'Exit file manager:\n\texit'
        print('Thank you for using Fima')
        return True
