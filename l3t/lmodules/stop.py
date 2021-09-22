import argparse
import sys
import os
from . import LModule, bash, yn, optionSelect


class Stop (LModule):
    """
        Stop node
    """
    NAME = "stop"
    DESCRIPTION = 'stop node'

    def parseArgs(self):
        self.args = self.parser.parse_args (sys.argv[2::])
        self.lnode.setPath(self.args.basepath)
        return self 

    def run(self):
        if not self.lnode.isRunning():
            print ('An instance of lisk-core is not running!')

        print ('Stopping Lisk')
        os.system('pm2 stop %s/pm2.conf.json' % self.args.basepath)
        