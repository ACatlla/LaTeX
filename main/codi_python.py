class Comptador(object):

    def __init__(self):
        self.c = 0

    def inc(self):
        self.c = self.c + 1

    def dec(self):
        self.c = self.c - 1

    def get(self):
        return self.c
