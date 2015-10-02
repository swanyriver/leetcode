class me(object):
    """docstring for me"""
    def __init__(self, arg,string):
        self.arg = arg
        self.string = string

    def __str__(self):
        return "%d->%s"%(self.arg,self.string)
    def __repr__(self):
        return self.__str__()

    def __eq__(self,other):
        return self.arg == other.arg

    def __hash__(self):
        return hash(self.arg)

        