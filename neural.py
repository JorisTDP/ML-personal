from itertools import accumulate
import math
import random 
import time

class Node:
    def __init__(self, value = None):
        self.links = []
        self.value = value
    
    def getValue(self):
        sum = 0 
        if self.value != None:
            sum = self.value
        else:      
            for link in self.links:
                sum += link.getValue()
        return sum
        

class Link:
    def __init__(self, n1, n2):
        self.weight = random.uniform(-1, 1)
        self.inputNode = n1
        
        n2.links.append(self)

    def getValue(self):
        return self.weight * self.inputNode.getValue()

symbolVecs = {'O': (1,0), 'X': {0, 1}}
symbolChars = dict ((key, value) for key, value in symbolVecs.items())

inputDim = 9
hiddenDim = 39
# hiddenDim = 10
outputDim = 2

side = 3
inNodes = [[Node() for column in range (side)] for row in range(side)]
outNodes = [Node() for i in range(2)]

nrOfRows = 3
nrOfColumns = 3

costThreshold = 0.09

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

def softMax(inVec):
    expVec = [math.exp (inScal) for inScal in inVec]
    aSum = sum (expVec)
    return [expScal / aSum for expScal in expVec]

def costFunc(outVec, modelVec): #gemiddelde berkenen ofzo, gemiddelde veranderen totdat costor laag is.
    return sum([(lambda x: x*x) (zipped[0] - zipped[1]) for zipped in zip(outVec, modelVec)])
    #sum = deltaX * deltaX + deltaY * deltaY


def computeAverageCost():

    accumulatedCost = 0

    for trainingsItem in trainingSet:

        for iRow in range(nrOfRows):
            for iColumn in range(nrOfColumns):
                inNodes [iRow][iColumn].value = trainingsItem[0][iRow][iColumn]

    accumulatedCost += costFunc(softMax([outNode.getValue() for outNode in outNodes]), symbolVecs[trainingsItem[1]])
    #print(accumulatedCost)
    return accumulatedCost / len(trainingSet)

def main():

    #compute average cost
    #iterate until the averagecost is as small as possible using a learning rate
    #change the weights of the links

    links = []
    for inRow in inNodes:
        for inNode in inRow:
            for outNode in outNodes:
                links.append(Link(inNode, outNode))

    averageCost = computeAverageCost()
    print(averageCost)

    # for node in inNodes:
    #     for n in node:
    #         print(n.value)

    while True:
        bestCost = 100

        if averageCost < costThreshold:
            print("======================================================")
            break

        # Change the weights of the links
        if averageCost < bestCost:
            bestCost = averageCost
            best_link = None

        for trainingsItem in trainingSet:
            # Set the input node values to the current training item

            # Compute the output values
            outValues = softMax([outNode.getValue() for outNode in outNodes])

            # Compute the target output values
            targetValues = outputDict[trainingsItem[1]]

            # Compute the error
            errors = [(targetValues[i] - outValues[i]) for i in range(outputDim)]

            learning_rate = 0.01
            # Backpropagation
            for i in range(outputDim):
                for j in range(3):
                    inNodes[i][j].value += errors[i]
                for link in outNodes[i].links:
                    #link.weight += errors[i] * link.inputNode.getValue()
                    link.weight += learning_rate
                    newCost = computeAverageCost()
                    if newCost < bestCost:
                        bestCost = newCost
                        best_link = link
                    link.weight -= learning_rate
            if best_link is not None:
                best_link.weight += learning_rate

            time.sleep(0.1)

        # Print the final average cost
        averageCost = computeAverageCost()
        print(f"Final average cost: {averageCost}")

    fCost = 0
    nCost = 0
    for testItem in testSet:

        fCost = costFunc(softMax([outNode.getValue() for outNode in outNodes]), symbolVecs[testItem[1]])
        #nCost = costFunc(softMax([outNode.getValue() for outNode in outNodes]), symbolVecs[testItem[2]])

        print(fCost)


    #print(finalCost / len(testSet))

    




    # while averageCost > costThreshold:
    #     bestCost = 0
    #     bestLink = None

    #     tempLinks = [outNode.links for outNode in outNodes]

    #     if averageCost < bestCost:
    #         bestCost = averageCost
    #     else:
    #         for i in range(len(tempLinks)):
    #             outNodes[i].links = tempLinks[i]

    

    # print(inNodes[0][2])

    # print(outNodes[0].getValue())
    # print(outNodes[1].getValue())

main()    
