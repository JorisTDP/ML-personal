from itertools import accumulate
import math
import random 
import time
import numpy as np

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

    def adaptWeight(self, cost):
        self.weight += learning_rate * cost * self.weight

    def getValue(self):
        return self.weight * self.inputNode.getValue()

symbolVecs = {'O': (1,0), 'X': {0, 1}}
symbolChars = dict ((key, value) for key, value in symbolVecs.items())

inputDim = 9
# hiddenDim = 10
outputDim = 2

learning_rate = 0.01

side = 3
inNodes = np.matrix([[Node(), Node(), Node()],
                        [Node(), Node(), Node()],
                        [Node(), Node(), Node()]])
outNodes = [Node() for i in range(2)]

nrOfRows = 3
nrOfColumns = 3

costThreshold = 0.001

trainingSet = [
    [
        np.matrix([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]]), 'O'
    ],
    [
        np.matrix([[0, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]]), 'O'
    ],
    [
        np.matrix([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]]), 'X'
    ],
    [
        np.matrix([[1, 0, 1],
                   [0, 1, 0],
                   [1, 0, 1]]), 'X'
    ]
]

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

def costFunc(outVec, modelVec): #gemiddelde berekenen, gemiddelde veranderen totdat costor laag is.
    return sum([(lambda x: x*x) (zipped[0] - zipped[1]) for zipped in zip(outVec, modelVec)])
    #sum = deltaX * deltaX + deltaY * deltaY


def computeAverageCost():

    accumulatedCost = 0

    for trainingsItem in trainingSet:

        matrix = trainingsItem[0]
        label = trainingsItem[1]
        print("Matrix:")
        for value in matrix.flat:
            print(value, end=" ")
            print()
        print()
        print("Label:", label)
        print()

        # for iRow in range(nrOfRows):
        #     for iColumn in range(nrOfColumns):
        #         inNodes[iRow][iColumn].value = trainingsItem[0][iRow][iColumn]

        inNodes[0][0].value = trainingsItem[0][0][0]

        for i in range(inNodes.shape[0]):
            for j in range(inNodes.shape[1]):
                print("Node[{}, {}]: {}".format(i, j, inNodes[i, j].value))

        #accumulatedCost += costFunc(softMax([outNode.getValue() for outNode in outNodes]), symbolVecs[trainingsItem[1]])
    #print(accumulatedCost)
    return accumulatedCost / len(trainingSet)

def testNetwork():

    correctPredictions = 0

    for testItem in testSet:
        for iRow in range(nrOfRows):
            for iColumn in range(nrOfColumns):
                inNodes [iRow][iColumn].value = testItem[0][iRow][iColumn]

        outputVec = softMax([outNode.getValue() for outNode in outNodes])
        predictedSymbol = 'X' if outputVec[0] < outputVec[1] else 'O'
        
        print("actual symbol: " + testItem[1])
        print("predicted symbol: " + predictedSymbol)
        print("O: " + str(outputVec[0]) + "  X: " + str(outputVec[1]))

        if predictedSymbol == testItem[1]:
            correctPredictions += 1



    print(f"Number of correct predictions: {correctPredictions}")
    print(f"Number of total predictions: {len(testSet)}")
    print(f"Accuracy: {correctPredictions / len(testSet)}")

def main():

    #compute average cost
    #iterate until the averagecost is as small as possible using a learning rate
    #change the weights of the links

    links = []
    for inRow in inNodes:
        for inNode in inRow:
            for outNode in outNodes:
                links.append(Link(inNode, outNode))

    for link in links:
        print(link.weight)

    averageCost = computeAverageCost()
    print(averageCost)
    counter = 0

    while True:
        bestCost = 10
        bestCostIncrease = 0
        counter+=1

        if averageCost < costThreshold:
            if(counter > 5000):
                break
            print("======================================================")
            #break

        # Change the weights of the links
        if averageCost < bestCost:
            bestCost = averageCost
            bestLink = None

        for trainingsItem in trainingSet:
            # Set the input node values to the current training item

            # Compute the output values
            outValues = softMax([outNode.getValue() for outNode in outNodes])

            # Compute the target output values
            targetValues = outputDict[trainingsItem[1]]
                                               
            # Compute the error
            errors = [(targetValues[i] - outValues[i]) for i in range(outputDim)]

            # Backpropagation
            for i in range(outputDim):
                for j in range(3):
                    inNodes[i][j].value += errors[i]
                for link in outNodes[i].links: 
                    link.adaptWeight(averageCost)

                    newAverage = computeAverageCost()
                    costIncrease = newAverage - averageCost

                    if abs (costIncrease) > abs (bestCostIncrease):
                        bestCostIncrease = costIncrease
                        bestLink = link

                    link.adaptWeight(-averageCost)

                bestLink.adaptWeight(-averageCost if bestCostIncrease > 0 else averageCost)
                averageCost = computeAverageCost()

        #print(f"Final average cost: {averageCost}")
        print("Final average cost: " + str(averageCost) + " " + '*' * int (averageCost * 120))
    
    testNetwork()

#for link in links:

main()    
