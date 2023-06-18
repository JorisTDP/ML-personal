import numpy as np
import math
import random 

class Node:
    def __init__(self, value=None):
        self.links = []
        self.value = value
    
    def getValue(self):
        if self.value is not None:
            return self.value
        else:      
            return sum(link.getValue() for link in self.links)

class Link:
    def __init__(self, n1, n2):
        self.weight = random.uniform(-1, 1)
        self.inputNode = n1
        n2.links.append(self)

    def adaptWeight(self, cost):
        self.weight += learning_rate * cost * self.weight

    def getValue(self):
        return self.weight * self.inputNode.getValue()

symbolVecs = {'O': np.array([1, 0]), 'X': np.array([0, 1])}

inputDim = 9
outputDim = 2

learning_rate = 0.01

side = 3
inNodes = np.array([[Node() for i in range(side)] for i in range(side)])
outNodes = np.array([Node() for i in range(outputDim)])

nrOfRows = 3
nrOfColumns = 3

costThreshold = 0.001

trainingSet = (
    (np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), 'O'),
    (np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]), 'O'),
    (np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]), 'X'),
    (np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]]), 'X')
)

testSet = (
    (np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), 'O'),
    (np.array([[1, 0, 1], [1, 0, 1], [1, 1, 0]]), 'O'),
    (np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1]]), 'O'),
    (np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]), 'O'),
    (np.array([[1, 0, 0], [1, 1, 1], [0, 0, 1]]), 'X'),
    (np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]]), 'X'),
    (np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]]), 'X'),
    (np.array([[1, 0, 0], [1, 1, 0], [1, 0, 0]]), 'X')
)      

outputDict = {'O': np.array([1, 0]), 'X': np.array([0, 1])}

def softMax(inVec): # calculates the softmax activation of an input vector
    expVec = np.exp(inVec)
    return expVec / np.sum(expVec)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def costFunc(outVec, modelVec): # calculates the mean squared error between outputvec and modelvec
    return np.sum((outVec - modelVec) ** 2)

def computeAverageCost():  # computes the average cost over the training set
    accumulatedCost = 0

    for trainingsItem in trainingSet:
        for iRow in range(nrOfRows):
            for iColumn in range(nrOfColumns):
                inNodes[iRow][iColumn].value = trainingsItem[0][iRow][iColumn]

        accumulatedCost += costFunc(softMax([outNode.getValue() for outNode in outNodes]), symbolVecs[trainingsItem[1]])

    return accumulatedCost / len(trainingSet)

def testNetwork(): # tests the trained network 
    correctPredictions = 0

    for testItem in testSet:
        for iRow in range(nrOfRows):
            for iColumn in range(nrOfColumns):
                inNodes[iRow][iColumn].value = testItem[0][iRow][iColumn]

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
    links = []
    for inRow in inNodes: #Connect all nodes to eachother in array called links
        for inNode in inRow:
            for outNode in outNodes:
                links.append(Link(inNode, outNode))

    for link in links:
        print(link.weight)

    averageCost = computeAverageCost()
    print(averageCost)
    counter = 0

    while True: # Training the neural network through backpropagation + steepest descent
        bestCost = 10
        bestCostIncrease = 0
        counter += 1

        if averageCost < costThreshold:
            if counter > 500:
                break
            print("======================================================")

        if averageCost < bestCost: #update bestcost
            bestCost = averageCost
            bestLink = None

        for trainingsItem in trainingSet:
            for i in range(nrOfRows):
                for j in range(nrOfColumns):
                    inNodes[i][j].value = trainingsItem[0][i][j]

            outValues = softMax([outNode.getValue() for outNode in outNodes])
            targetValues = outputDict[trainingsItem[1]]
            errors = targetValues - outValues

            for i in range(outputDim):
                for j in range(3):
                    inNodes[i][j].value += errors[i]
                for link in outNodes[i].links: 
                    link.adaptWeight(averageCost)

                    newAverage = computeAverageCost()
                    costIncrease = newAverage - averageCost

                    if abs(costIncrease) > abs(bestCostIncrease):
                        bestCostIncrease = costIncrease
                        bestLink = link

                    link.adaptWeight(-averageCost)

                if bestCostIncrease > 0:
                    bestLink.adaptWeight(-averageCost)
                else:
                    bestLink.adaptWeight(averageCost)

                averageCost = computeAverageCost()

        print("Final average cost: " + str(averageCost) + " " + '*' * int(averageCost * 120))

    testNetwork()

main()   
