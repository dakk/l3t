from .lmodules import bash 
import json 

class LiskNode:
    def __init__(self):
        pass 

    def getPath(self):
        return self.basepath

    def setPath(self, basepath):
        self.basepath = basepath + '/lisk-core/bin/lisk-core'

        # if self.isRunning():
        #     print ("Node is running on %s with version %s at height %d" % (self.getNetwork(), self.getVersion(), self.getBlockHeight()))
        # else:
        #     print ("Node is not running")

    def isRunning(self):
        """ Return true if the node is running """
        try:
            return self.getNodeInfo()['height'] > 0
        except:
            return False

    def getNodeInfo(self):
        return json.loads(bash('%s node:info' % self.basepath).value())

    def getForgingStatus(self):
        return json.loads(bash('%s forging:status' % self.basepath).value())

    def getVersion(self):
        """ Return lisk-core version """
        return self.getNodeInfo()['version']

    def getBlockHeights(self):
        """ Return block height from different source """
        pass 

    def networkOfIdentifier(self, iden):
        if iden == '4c09e6a781fc4c7bdb936ee815de8f94190f8a7519becd9de2081832be309a99':
            return 'mainnet'
        else:
            return 'testnet'

    def getNetwork(self):
        return self.networkOfIdentifier(self.getNodeInfo()['networkIdentifier'])

    def getBlockHeight(self):
        self.getNodeInfo()['height']


    def enableForging(self, address, height, maxheightpreviouslyforged, maxheightprevoted, password = None):
        cmd = '%s forging:enable "%s" "%d" "%d" "%d"' % (self.basepath, address, height, maxheightpreviouslyforged, maxheightprevoted)
        if password:
            cmd += ' --password "%s"' % password 
        return bash(cmd).value()

