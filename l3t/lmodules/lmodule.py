import sys
from subprocess import PIPE, Popen
SUBPROCESS_HAS_TIMEOUT = True


class bash(object):
    "This is lower class because it is intended to be used as a method."

    def __init__(self, *args, **kwargs):
        self.p = None
        self.stdout = None
        self.bash(*args, **kwargs)

    def bash(self, cmd, env=None, stdout=PIPE, stderr=PIPE, timeout=None, sync=True):
        self.p = Popen(
            cmd, shell=True, stdout=stdout, stdin=PIPE, stderr=stderr, env=env
        )
        if sync:
            self.sync(timeout)
        return self

    def sync(self, timeout=None):
        kwargs = {'input': self.stdout}
        if timeout:
            kwargs['timeout'] = timeout
            if not SUBPROCESS_HAS_TIMEOUT:
                raise ValueError(
                    "Timeout given but subprocess doesn't support it. "
                    "Install subprocess32 and try again."
                )
        self.stdout, self.stderr = self.p.communicate(**kwargs)
        self.code = self.p.returncode
        return self

    def __repr__(self):
        return self.value()

    def __unicode__(self):
        return self.value()

    def __str__(self):
        return self.value()

    def __nonzero__(self):
        return self.__bool__()

    def __bool__(self):
        return bool(self.value())

    def value(self):
        if self.stdout:
            return self.stdout.strip().decode(encoding='UTF-8')
        return ''

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

    def __init__(self, parser, lnode):
        self.parser = parser
        self.lnode = lnode

    def parseArgs(self):
        raise Exception('Abstract parseArgs()')

    def run(self):
        raise Exception('Abstract run()')