import argparse
import sys
from . import LModule

SNAPSHOT_SOURCE = {
    'mainnet': [
        'https://snapshots.lisk.io/main/',
        'https://snapshot.lisknode.io/',
        'https://snapshot.liskworld.info/'
    ], 
    'testnet': [
        'https://testnet3-snapshot.lisknode.io/'
    ]
}

class Rebuild (LModule):
    """
        Rebuild node from snapshot
    """
    NAME = "rebuild"
    DESCRIPTION = 'rebuild node from snapshot'

    def parseArgs(self):
        parser = argparse.ArgumentParser()
                        
        # parser.add_argument('--network', type=str, dest='network', action='store',
        #             default=None, required=True,
        #             help='force network to mainnet or testnet (default: auto)')

        self.margs = parser.parse_args (sys.argv[2::])

    def run(self):
        print ('Rebuilding...')