import argparse
import sys
import subprocess
import os
import requests
from . import LModule, optionSelect, yn, bash

DOWNLOAD_URI = "https://downloads.lisk.io/lisk/"

class Install (LModule):
    """
        Install lisk-core
    """
    NAME = "install"
    DESCRIPTION = 'install lisk-core'

    def parseArgs(self):                        
        self.parser.add_argument('--network', type=str, dest='network', action='store',
                    default=None, required=True,
                    help='force network to mainnet or testnet')

        self.args = self.parser.parse_args (sys.argv[2::])

    def run(self):
        if self.lnode.isRunning():
            print ('An instance of lisk-core is running!')
            sys.exit(0)
        
        print ('Installing lisk-core for network %s...' % self.args.network)

        versions = requests.get(DOWNLOAD_URI + self.args.network + '/').text.split('href="')[2::]
        versions = map(lambda v: v.split('"')[0], versions)
        versions = filter(lambda v: v.find('/') != -1, versions)
        versions = map(lambda v: v.replace('/', ''), versions)
        versions = list(versions)
        selected = optionSelect(versions, prompt="Version: ", header="Which version do you want to install?")

        print ("Selected version %s" % selected)

        uri = DOWNLOAD_URI + self.args.network + '/' + selected + '/'
        fname = 'lisk-core-v' + selected + '-linux-x64.tar.gz'
        tar = uri + fname 
        sha = uri + fname + '.SHA256' 
        basedir = self.args.basepath
        
        if os.path.isdir(basedir + '/lisk-core'):
            if not yn("Directory %s/lisk-core exists, overwrite?" % basedir):
                print("Exiting.")
                sys.exit(0)
            else:
                print ('Removing %s/lisk-core...' % basedir)
                bash('rm -r %s/lisk-core' % basedir)

        print ("Downloading %s..." % fname)
        bash('rm %s/lisk-core-v*' % basedir)
        bash('curl %s -o %s/%s' % (tar, basedir, fname), stderr=subprocess.STDOUT)
        bash('curl %s -o %s/%s.SHA256' % (sha, basedir, fname), stderr=subprocess.STDOUT)
        
        out = bash('cd %s && sha256sum %s.SHA256 -c' % (basedir, fname)).value()
        if out.find('OK') == -1:
            print ("Invalid sha256, corrupted file.")
            sys.exit(0)

        print ("Extracting %s to %s..." % (fname, basedir))
        bash('cd %s && tar -xf %s' % (basedir, fname))

        print ("Writing pm2 starter %s/pm2.conf.json..." % basedir)
        f = open(basedir + '/pm2.conf.json', 'w')
        f.write('''{
  "name": "lisk-core",
  "script": "%s/lisk-core/bin/lisk-core start --api-ws",
  "env": {
    "LISK_NETWORK": "%s",
    "LISK_CONFIG_FILE": "%s/lisk-core/config/%s/custom-config.json"
  }
}
''' % (basedir, self.args.network, basedir, self.args.network))
        f.close()

        print ("Node is ready; start with: pm2 start %s/pm2.conf.json" % basedir)