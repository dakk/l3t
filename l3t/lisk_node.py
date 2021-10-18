from .lmodules import bash 
import json 
import time

class LiskNode:
    def __init__(self):
        self.cache = None

    def getPath(self):
        return self.basepath

    def setPath(self, basepath):
        self.basepath = basepath + '/lisk-core/bin/lisk-core'

        # if self.isRunning():
        #     print ("Node is running on %s with version %s at height %d" % (self.getNetwork(), self.getVersion(), self.getBlockHeight()))
        # else:
        #     print ("Node is not running")

    def isRunning(self, cached = False):
        """ Return true if the node is running """
        try:
            return self.getNodeInfo(cached)['height'] > 0
        except:
            return False

    def waitUntilSynced(self):
        """ Wait until the node is synced """
        while not self.isSynced():
            print ("=> Node is syncing, current height is %d" % self.getBlockHeight(True))
            time.sleep(5)

    def getNodeInfo(self, cached = False):
        if cached and self.cache != None:
            return self.cache 
        ni = json.loads(bash('%s node:info' % self.basepath).value())
        self.cache = ni
        return ni

    def isSynced(self, cached = False):
        """ Return true if the node is synced """
        try:
            return not self.getNodeInfo(cached)['syncing']
        except:
            return False

    def getForgingStatus(self):
        return json.loads(bash('%s forging:status' % self.basepath).value())

    def getVersion(self, cached = False):
        """ Return lisk-core version """
        return self.getNodeInfo(cached)['version']

    def getBlockHeights(self, cached = False):
        """ Return block height from different source """
        pass 

    def networkOfIdentifier(self, iden):
        if iden == '4c09e6a781fc4c7bdb936ee815de8f94190f8a7519becd9de2081832be309a99':
            return 'mainnet'
        else:
            return 'testnet'

    def getNetwork(self, cached = False):
        return self.networkOfIdentifier(self.getNodeInfo(cached)['networkIdentifier'])

    def getBlockHeight(self, cached = False):
        return self.getNodeInfo(cached)['height']


    def enableForging(self, address, height, maxheightpreviouslyforged, maxheightprevoted, password = None):
        cmd = '%s forging:enable "%s" "%d" "%d" "%d"' % (self.basepath, address, height, maxheightpreviouslyforged, maxheightprevoted)
        if password:
            cmd += ' --password "%s"' % password 
        return bash(cmd).value()

