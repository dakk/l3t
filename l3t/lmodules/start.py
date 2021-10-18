import argparse
import sys
import os
from . import LModule, bash, yn, optionSelect


class Start (LModule):
    """
        Start node
    """
    NAME = "start"
    DESCRIPTION = 'start node'

    def parseArgs(self):
        self.args = self.parser.parse_args (sys.argv[2::])
        self.lnode.setPath(self.args.basepath)
        return self 

    def run(self):
        if self.lnode.isRunning():
            print ('An instance of lisk-core is running!')
            sys.exit(0)

        print ('=> Starting Lisk')
        os.system('pm2 start %s/pm2.conf.json' % self.args.basepath)
        