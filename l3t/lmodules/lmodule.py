class LModule:
    NAME = None
    DESCRIPTION = None

    def __init__(self, args, lnode):
        self.args = args 
        self.lnode = lnode

    def parseArgs(self):
        raise Exception('Abstract parseArgs()')


    def run(self):
        raise Exception('Abstract run()')