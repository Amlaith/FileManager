import os


class Pathfinder:
    def __init__(self, root):
        self.root = root
        self.working_directory = root

    def make_path(self, tail):
        head = self.working_directory.split(os.sep)
        tail = tail.split('/')

        while tail[0] and tail[0][0] == '^':
            tail[0] = tail[0][1:]
            head = head[:-1]

        path = os.path.join(*head, *tail).replace(':', ':' + os.sep)

        if self.root not in path:
            raise EnvironmentError
        return path

    def change_wd(self, directory):
        try:
            os.chdir(directory)
        except Exception as e:
            return f'Unable to change directory: {e}'
        else:
            self.working_directory = directory
            return f'Current working directory: {os.getcwd()}'

    def _set_root(self, root):
        self.root = root
