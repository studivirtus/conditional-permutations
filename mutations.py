#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Michael
#
# Created:     29/04/2014
# Copyright:   (c) Michael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

truthTable = (1, 0, 0, 0)
enter = ['a','b','c','d','e']
modEnter = ()
mutations = [
    [0,3,2,4,1],
    [0,3,4,1,2],
    [0,2,3,1,4],
    [0,1,3,4,2],
    [0,3,1,2,4,]]


from itertools import cycle

def mutatate (source, muta, rev):
    mutation = [0,0,0,0,0]
    mutaCycle = cycle(muta)
    if rev:
        muta.reverse()
    nextel = mutaCycle.__next__()
    i = 0
    while i < 5:
        #print(nextel)
        mutation[(mutaCycle.__next__())] = source[nextel]
        thisel, nextel = nextel, mutaCycle.__next__()
        #print(mutation)
        i += 1
    return mutation

import bisect
import operator
class node:
    nValue = 0
    pNode = 0
    nCost = 0
    nDepth = 0
    maxDepth = 0
    def __init__(self, nodeValue,parentNode,nodeCost,nodeDepth,maxDepth):
        self.nValue = nodeValue
        self.pNode = parentNode
        self.nCost = nodeCost
        self.nDepth = nodeDepth
        self.maxDepth = maxDepth

    def __lt__(self,other):
        return self.nCost < other.nCost
    def __gt__(self,other):
        return self.nCost > other.nCost

    def hasChildren(self):
        """verify that the node has children"""
        """NOTE if maxDepth set to '0' maxDepth is infinite"""
        if (self.nDepth < self.maxDepth or self.maxDepth == 0):
            return True
        return False
    def getChildren(self,pNode):
        """get children of a node"""
        chillens = []
        for i in mutations:
            m = mutatate(self.nValue,i,False)
            chillens.append(node(m,pNode,self.nCost,(pNode.nDepth + 1),pNode.maxDepth))
        for i in mutations:
            m = mutatate(self.nValue,i,True)
            chillens.append(node(m,pNode,self.nCost,(pNode.nDepth + 1),pNode.maxDepth))
        return[chillens]


class depthFirstSearch():
    """ Completes a depth first search"""
    """NOTE providing '0' as a 'maxDepth' value allows an infinit search depth"""
    frontier = list() #sorted list
    nodesVisited = list()
    goal = 0
    depthLimit = 0
    def __init__(self,firstNode,goalValue,depthLimit):
        self.frontier.append(firstNode)
        self.goal = goalValue
        self.depthLimit = depthLimit

    def explore(self):
        """Explore for a solution"""
        curNode = node(0,0,0,0,0)
        solutionNode = (0,0,0,0,0)
        found = False

        #test child nodes
        while((not self.frontierIsEmpty()) and (not found)):
            reverseChildren = list()
            """print('-----------------new-----------------')#DEBUG
            print('current frontier:')#DEBUG
            self.printlist(self.frontier)#DEBUG
            print('current visited nodes:')#DEBUG
            self.printlist(self.nodesVisited)#DEBUG"""
            curNode = self.frontier.pop(0)
            #print("current node: %i" %curNode.nValue) #DEBUG
            if self.goalReached(curNode.nValue):
                found = True
                solutionNode = curNode
                self.addNodesVisited(curNode)
                break
            self.addNodesVisited(curNode)
            if (curNode.nDepth < self.depthLimit or  self.depthLimit == 0):
                if curNode.hasChildren():
                    children = curNode.getChildren(curNode)
                    for x in range(len(children)):
                        reverseChildren.insert(0,children.pop(0))
                    for child in reverseChildren:
                        self.addToFrontier(child)

        if(found):
            print("Depth first search FOUND A SOLUTION %i" % solutionNode.nValue)
            print("here are the nodes visited:")
            self.printlist(self.nodesVisited)
        elif not found and self.frontierIsEmpty():
            print("FAILURE, Depth first search did not find a solution")
            print("here are the nodes visited:")
            self.printlist(self.nodesVisited)

    def atMaxDepth(self,curNode):
        if curNode.nDepth == self.depthLimit:
            return True
        return False


    def addNodesVisited(self,curNode):
        self.nodesVisited.append(curNode)

    def frontierIsEmpty(self):
        """check if frontier is empty"""
        if (len(self.frontier) > 0):
            return False
        return True

    def addToFrontier(self,curNode):
        """add node to frontier"""
        self.frontier.extend(curNode)


    def goalReached(self,nValue):
        pass
       # """YAY GOAL IS REACHED WE"RE DONE"""
       # if nValue == self.goal:
       #     return True
       # return False

    def printlist(self,list):
        """Utility for printing lists"""
        for item in list:
            print(item.nValue,end=', ')
        print('')

def main():
    pass


if __name__ == '__main__':
    main()
    goalNode = 15
    maxNodeDepth = 5 #Nodes beyond this level don't have children
    depthLimit = 4 #Set maximun level for DFS to search 0 = INFINITY

    startingNode = node(enter,0,0,0,maxNodeDepth)

    DFS = depthFirstSearch(startingNode,goalNode,depthLimit)
    DFS.explore()

print("DONE")