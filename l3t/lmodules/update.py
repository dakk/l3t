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
        # parser.add_argument('--network', type=str, dest='network', action='store',
        #             default=None, required=True,
        #             help='force network to mainnet or testnet (default: auto)')

        self.args = self.parser.parse_args (sys.argv[2::])
        self.lnode.setPath(self.args.basepath)

    def run(self):
        print ('Updating lisk-core...')