import argparse
import sys
import os
import time
from . import LModule, Stop, Start, Install

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
        return self 

    def run(self):
        if not self.lnode.isRunning():
            print ('Lisk-core is not running!')
            sys.exit(0)

        print ('Updating lisk-core...')
        i = self.lnode.getNodeInfo()
        net = self.lnode.networkOfIdentifier(i['networkIdentifier'])
        print ('Current version is %s' % i['version'])
        os.system('mv %s/lisk-core %s/lisk-core_back' % (self.args.basepath, self.args.basepath))
        
        Stop(self.parser, self.lnode).injectArgs(self.args).run()

        Install(self.parser, self.lnode).injectArgs(self.args).run(network=net)

        os.system('cp %s/lisk-core_back/config/%s/custom-config.json %s/lisk-core/config/%s/custom-config.json' % (self.args.basepath, net, self.args.basepath, net))

        Start(self.parser, self.lnode).injectArgs(self.args).run()


