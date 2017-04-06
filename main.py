import ID3
import sys
import Node
import Accuracy
import csv
from collections import defaultdict

def main():
    directory="data_sets1/"
    # directory="data_sets2/"
    # Comment one of the above lines

    L = int(sys.argv[1])
    K = int(sys.argv[2])
    train_file=str(sys.argv[2]) ;
    test_file=str(sys.argv[3]);
    train_file = directory + sys.argv[3]
    validation_file = directory + sys.argv[4]
    test_file = directory + sys.argv[5]
    yesno = str(sys.argv[6])


    decisionTree = ID3.DTree(train_file)
    if yesno == "yes":
        print "Decision Tree before Pruning:"
        print decisionTree

    accuracy = Accuracy.Accuracy(test_file)
    accuracy.calculateAccuracy(decisionTree.root)
    print "Accuracy before Pruning:"
    accuracy.displayAccuracy()

    decisionTree.pruneTree(L, K, validation_file)
    if yesno == "yes":
        print "Decision Tree after Pruning:"
        print decisionTree
    accuracy.calculateAccuracy(decisionTree.root)
    print "Accuracy after Pruning:"
    accuracy.displayAccuracy()

def csvParser(self, filename):
    self.data = []
    with open(filename,'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        count = 0
        for row in csvreader:
            # print row
            if count == 0:
                self.attributeNames = row[:-1]
            else:
                self.data.append([int(i) for i in row])
            count += 1

    self.attributes = range(len(self.attributeNames))
    self.trainingValues = range(len(self.data))
    self.Class = [row[-1] for row in self.data]
    return self

if __name__ == '__main__':
    main()
