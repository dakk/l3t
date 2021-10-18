import argparse
import sys
import os
import time
from . import LModule, bash, yn, optionSelect, Start, Stop

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
        self.args = self.parser.parse_args (sys.argv[2::])
        self.lnode.setPath(self.args.basepath)
        return self 

    def run(self):
        if not self.lnode.isRunning():
            print ('Lisk-core is not running!')
            sys.exit(0)

        net = self.lnode.getNetwork()

        print ('=> Rebuilding node from %s snapshot...' % net)
        sources = SNAPSHOT_SOURCE[net]
        selected = optionSelect(sources, prompt="Snapshot source: ", header="Which snapshot source do you want to use?")

        print ('=> Downloading snapshot...')
        uri = selected + 'blockchain.db.tar.gz'
        bash('rm -f %s/blockchain.db.tar.gz*' % self.args.basepath)
        os.system('%s blockchain:download --url %s --output %s' % (self.lnode.getPath(), uri, self.args.basepath))

        print ("=> Importing snapshot...")
        Stop(self.parser, self.lnode).injectArgs(self.args).run()
        time.sleep(3)
        os.system('%s blockchain:import %s/blockchain.db.tar.gz --force' % (self.lnode.getPath(), self.args.basepath, ))
        Start(self.parser, self.lnode).injectArgs(self.args).run()
        bash('rm -f %s/blockchain.db.tar.gz*' % self.args.basepath)