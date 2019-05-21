import os
import datetime

TERMINAL_TAGS = ['exit', 'end', 'over', 'stop']

class Log:
    def __init__(self, dir):
        self.dir = dir

    def log(self, session, tag):
        """session: [[sys, usr], [sys, usr], ...]"""
        sess_str = "--{}--\n--tag: {}--\n".format(get_time_str(), tag)
        for sys, usr in session:
            sess_str += '{}\n{}\n\n'.format(sys.strip(), usr.strip())
        self._log(sess_str)


    def _log(self, string):
        with open(self.dir, 'a+') as f:
            f.write(string)
            f.close()

class DialogSession:
    def __init__(self):
        self.history = []

    def append(self, sys, usr):
        self.history.append([sys, usr])

    def get_history(self):
        return self.history

    def clear(self):
        self.history = []


def get_time_str():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))