import argparse
import sys
import os
from . import LModule, bash, yn, optionSelect


class Info (LModule):
    """
        Info node
    """
    NAME = "info"
    DESCRIPTION = 'Info node'

    def parseArgs(self):
        self.args = self.parser.parse_args (sys.argv[2::])
        self.lnode.setPath(self.args.basepath)

    def run(self):
        if not self.lnode.isRunning():
            print ('An instance of lisk-core is not running!')
            sys.exit(0)

        i = self.lnode.getNodeInfo()
        print (i)
        print()
        print ('Node Info:')
        print('\tnetwork: %s' % self.lnode.networkOfIdentifier(i['networkIdentifier']))
        for x in ['version', 'syncing', 'height', 'unconfirmedTransactions']:
            print ('\t%s: %s' % (x, i[x]))  
        print (i)