class cat(object):
    """docstring for cat"""
    def __init__(self, name):
        self.name = name

    def talk(self):
        print self.name, " says: meow"

    def yell(self):
        print self.name, "says: MEOW"

    def swap(self):
        self.talk = self.yell
        