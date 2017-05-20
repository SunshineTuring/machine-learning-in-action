# -*- coding: utf-8 -*-
import trees
import treePlotter

dataFileName = "salarytrain.dat"
testFileName = "test.dat"
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['Age', 'Workclass', 'Fnlwgt', 'Education', 'Education-num', 'Marital-status', 'Occupation', \
              'Relationship', 'Race', 'Sex', 'Capital-loss', 'Hours-per-week', 'Native-country']
    # Age Fnlwgt Education-num Capital-gain  Capital-loss Hours-per-week
    dataFile = open(dataFileName,'r')
    dataSet = []
    while(1):
        line = dataFile.readline()
        if line == "":
            break
        line = line.strip().split()
        dataSet.append(line)

    return dataSet,labels


if __name__ =="__main__":

    dataSet, labels = createDataSet()
    inTree = trees.createTree(dataSet, labels)

    treePlotter.createPlot(inTree)
    # treePlotter.createPlot(inTree)
    dataSet = ['25', 'Private', '226802', '11th', '7', 'Never-married',' Machine-op-inspct'\
        , 'Own-child', 'Black', 'Male', '0','0', '40', 'United-States']
    labels = ['Age', 'Workclass', 'Fnlwgt', 'Education', 'Education-num', 'Marital-status', 'Occupation', \
              'Relationship', 'Race', 'Sex', 'Capital-gain','Capital-loss', 'Hours-per-week', 'Native-country']
    print trees.classify(inTree, labels, dataSet)