import argparse
import sys
from . import LModule

class Update (LModule):
    """
        Rebuild node from snapshot
    """
    NAME = "update"
    DESCRIPTION = 'update lisk-core'

    def parseArgs(self):
        parser = argparse.ArgumentParser()
                        
        # parser.add_argument('--network', type=str, dest='network', action='store',
        #             default=None, required=True,
        #             help='force network to mainnet or testnet (default: auto)')

        self.margs = parser.parse_args (sys.argv[2::])

    def run(self):
        print ('Updating lisk-core...')