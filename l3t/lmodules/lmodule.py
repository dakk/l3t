def optionSelect(options, header="Options:", prompt="Choice: "):
    i = 1
    print (header)
    for x in options:
        print (' %d) %s' % (i, x))
        i += 1

    r = 0
    while r < 1 or r > len(options):
        r = int(input(prompt))
    selected = options[r-1]
    return selected

def yn(header="Do you confirm?"):
    print (header)
    print (' y) yes')
    print (' n) no')
    
    r = ''
    while r != 'n' and r != 'y':
        r = input('yn: ').lower()[0]
    
    return r == 'y'

class LModule:
    NAME = None
    DESCRIPTION = None
    network = 'auto'

    def __init__(self, args, lnode):
        self.args = args 
        self.lnode = lnode

    def parseArgs(self):
        raise Exception('Abstract parseArgs()')

    def run(self):
        raise Exception('Abstract run()')