import argparse
import sys
import os
from . import LModule, bash, yn, optionSelect


class Logs (LModule):
    """
        Logs node
    """
    NAME = "logs"
    DESCRIPTION = 'Logs node'

    def parseArgs(self):
        self.args = self.parser.parse_args (sys.argv[2::])
        self.lnode.setPath(self.args.basepath)

    def run(self):
        if not self.lnode.isRunning():
            print ('An instance of lisk-core is not running!')
            sys.exit(0)

        print ('Tailing logs')
        os.system('pm2 logs lisk-core')
        