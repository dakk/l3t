import argparse
import sys
from . import LModule

class EnableForging (LModule):
    """
        Rebuild node from snapshot
    """
    NAME = "enable-forging"
    DESCRIPTION = 'enable forging'

    def parseArgs(self):
        parser = argparse.ArgumentParser()
                        
        parser.add_argument('--password', type=str, dest='password', action='store',
                    default=None, required=False,
                    help='set encryption password')

        self.margs = parser.parse_args (sys.argv[2::])
        self.lnode.setPath(self.args.basepath)

    def run(self):
        if not self.lnode.isRunning():
            print ('An instance of lisk-core is not running!')
            sys.exit(0)

        i = self.lnode.getInfo()

        if i['syncing']:
            print ('Node is syncing, cannot enable forging.')
            sys.exit(0)

        print ('Enabling forging...')
        f = self.lnode.getForgingStatus()

        for delegate in f:
            if delegate['forging']:
                print ('Forging already enabled for delegate %s, skipping' % delegate['address'])
                continue

            en = self.lnode.enableForging(delegate['address'], delegate['height'], delegate['maxHeightPreviouslyForged'], delegate['maxHeightPrevoted'])
            print(en)
            print ('Forging enabled for %s' % delegate['address'])