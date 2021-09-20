class LiskNode:
    def __init__(self):
        if self.isRunning():
            print ("Node is running on %s with version %s at height %d" % (self.getNetwork(), self.getVersion(), self.getBlockHeight()))
        else:
            print ("Node is not running")

    def getBaseDir(self):
        return '/home/lisk/'

    def isRunning(self):
        """ Return true if the node is running """
        pass 

    def getVersion(self):
        """ Return lisk-core version """
        pass 

    def getBlockHeights(self):
        """ Return block height from different source """
        pass 

    def getNetwork(self):
        pass 

    def getBlockHeight(self):
        pass  

    def getForgingInfo(self):
        pass 

    def enableForging(self, a, b, c):
        pass 

    def stop(self):
        pass 

    def start(self):
        pass 