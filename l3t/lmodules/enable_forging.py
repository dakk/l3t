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
                        
        # parser.add_argument('--network', type=str, dest='network', action='store',
        #             default=None, required=True,
        #             help='force network to mainnet or testnet (default: auto)')

        self.margs = parser.parse_args (sys.argv[2::])
        self.lnode.setPath(self.args.basepath)

    def run(self):
        print ('Enabling forging...')