import argparse
import sys
import os
import requests
from . import LModule, optionSelect

DOWNLOAD_URI = "https://downloads.lisk.io/lisk/"

class Install (LModule):
    """
        Install lisk-core
    """
    NAME = "install"
    DESCRIPTION = 'install lisk-core'

    def parseArgs(self):
        parser = argparse.ArgumentParser()
                        
        parser.add_argument('--network', type=str, dest='network', action='store',
                    default=None, required=True,
                    help='force network to mainnet or testnet')

        self.margs = parser.parse_args (sys.argv[2::])

    def run(self):
        if self.lnode.isRunning():
            print ('An instance of lisk-core is running!')
            sys.exit(0)
        
        print ('Installing lisk-core for network %s...' % self.margs.network)

        versions = requests.get(DOWNLOAD_URI + self.margs.network + '/').text.split('href="')[2::]
        versions = map(lambda v: v.split('"')[0], versions)
        versions = filter(lambda v: v.find('/') != -1, versions)
        versions = map(lambda v: v.replace('/', ''), versions)
        versions = list(versions)
        selected = optionSelect(versions, prompt="Version: ", header="Which version do you want to install?")

        print ("Selected version %s" % selected)

        uri = DOWNLOAD_URI + self.margs.network + '/' + selected + '/'
        fname = 'lisk-core-v' + selected + '-linux-x64.tar.gz'
        tar = uri + fname 
        sha = uri + fname + 'SHA256' 
        basedir = self.lnode.getBaseDir()

        print ("Downloading...")
        os.system('rm %slisk-core-*' % basedir)
        os.system('wget %s %s' % (tar, basedir))
        os.system('wget %s %s' % (sha, basedir))
        os.system('sha256sum %s%s.SHA256 -c' % (basedir, fname))

        print ("Extracting...")
        os.system('tar -xf %s%s' % (basedir, fname))