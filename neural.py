from itertools import accumulate

symbolVecs = {'O': (1,0), 'X': {0, 1}}
#symbolChars = dict ((value, key) for key, value in symbolVecs.items())

inputDim = 9
hiddenDim = 39
# hiddenDim = 10
outputDim = 2

maxCost = 0.01

trainingSet = (
    ((
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0)
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 1, 1),
        (0, 1, 0)
    ), 'X'),
    ((
        (1, 0, 1),
        (0, 1, 0),
        (1, 0, 1)
    ), 'X')
)

testSet = (
    ((
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ), 'O'),
    ((
        (1, 0, 1),
        (1, 0, 1),
        (1, 1, 0)
    ), 'O'),
    ((
        (1, 0, 1),
        (0, 0, 0),
        (1, 0, 1)
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0)
    ), 'O'),
    ((
        (1, 0, 0),
        (1, 1, 1),
        (0, 0, 1)
    ), 'X'),
    ((
        (0, 0, 1),
        (1, 1, 1),
        (1, 0, 0)
    ), 'X'),
    ((
        (0, 0, 0),
        (1, 1, 1),
        (0, 0, 0)
    ), 'X'),
    ((
        (1, 0, 0),
        (1, 1, 0),
        (1, 0, 0)
    ), 'X')
)      

outputDict = {'O': (1, 0), 'X': (0, 1)}

#costfunc heeft jarno

def costFunc(outVec, modelVec): #gemiddelde berkenen ofzo, gemiddelde veranderen totdat costor laag is.
    deltaX = modelVec[0] - outVec[0]
    deltaY = modelVec[1] - outVec[1]

    sum = deltaX * deltaX + deltaY * deltaY
    return sum

class neural:
    def __init__(self):
        pass
    def function(self):
        print("activate func")

class Node:
    def __init__(self):
        self.links = []
        self.bias = None
    
    def getValue(self):
        if self.links:
            sum = 0
            for link in links:
                sum += link.getValue()
            return sum
        else:
            return 0 #storedValue

class Link:
    def __init__(self, n1, n2):
        self.weight = 1
        self.inputNode = n1
        
        n2.links.append(self)

    def getValue(self):
        return self.weight * self.inputNode.bias

def computeAverageCost():

    accumulatedCost - 0

    for trainingsItem in trainingSet:

        for iRow in range(nrOfRows):
            for iColumn in range(nrOfColumns):
                inNodes [iRow][iColumn].value = traininsItem[0][iRow][iColumn]

    accumulatedCost += costFunc(softmax([outNode.getValue() for outNode in outNodes]), symbolVecs[trainingsItem[1]])

    return accumulatedCost / len (trainingSet)

side = 3
inNodes = [[Node() for column in range (side)] for row in range(side)]

print(inNodes[0][2])
# inNodes =   (   (Node(),Node(), Node()),
#                 (Node(),Node(), Node()),
#                 (Node(),Node(), Node())
#             )

outNodes = [Node() for i in range(2)]

links = []
for inRow in inNodes:
    for inNode in inRow:
        for outNode in outNodes:
            links.append(Link(inNode, outNode))

print(outNodes[0].getValue())
print(outNodes[1].getValue())
