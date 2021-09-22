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
        f = self.lnode.getForgingStatus()
        print (i)
        print(f)
        print()
        print ('Node Info:')
        print('\tnetwork: %s' % self.lnode.networkOfIdentifier(i['networkIdentifier']))
        for x in ['version', 'syncing', 'height', 'unconfirmedTransactions']:
            print ('\t%s: %s' % (x, i[x]))

        for x in f:
            print('\n')
            for y in x:
                print('\t%s: %s', str(x[y]))
            