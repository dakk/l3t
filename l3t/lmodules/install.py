import argparse
import sys
from . import LModule

class Install (LModule):
    """
        Rebuild node from snapshot
    """
    NAME = "install"
    DESCRIPTION = 'install lisk-core'

    def parseArgs(self):
        parser = argparse.ArgumentParser()
                        
        # parser.add_argument('--network', type=str, dest='network', action='store',
        #             default=None, required=True,
        #             help='force network to mainnet or testnet (default: auto)')

        self.margs = parser.parse_args (sys.argv[2::])

    def run(self):
        print ('Installing lisk-core...')