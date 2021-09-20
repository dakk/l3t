from .lmodules import bash 
import json 

class LiskNode:
    def __init__(self):
        if self.isRunning():
            print ("Node is running on %s with version %s at height %d" % (self.getNetwork(), self.getVersion(), self.getBlockHeight()))
        else:
            print ("Node is not running")

    def isRunning(self):
        """ Return true if the node is running """
        try:
            return self.getNodeInfo()['height'] > 0
        except:
            return False

    def getNodeInfo(self):
        return json.loads(bash('lisk-core node:info').value())

    def getVersion(self):
        """ Return lisk-core version """
        return self.getNodeInfo()['version']

    def getBlockHeights(self):
        """ Return block height from different source """
        pass 

    def getNetwork(self):
        if self.getNodeInfo()['networkIdentifier'] == '4c09e6a781fc4c7bdb936ee815de8f94190f8a7519becd9de2081832be309a99':
            return 'mainnet'
        else:
            return 'testnet'

    def getBlockHeight(self):
        self.getNodeInfo()['height']

    def getForgingInfo(self):
        pass 

    def enableForging(self, a, b, c):
        pass 

    def stop(self):
        bash('pm2 stop lisk-core')

    def start(self):
        bash('pm2 start lisk-core')