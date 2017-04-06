Run the following command on the prompt:

python main.py 7 2 training_set.csv validation_set.csv test_set.csv yes/no
-where 7 and 2 are values for L and K
-yes/no is to print the tree or not to

The ID3 file has calculation of bestAttribute using the Entropy Heuristic. For output using the variance impurity heuristic, uncomment Line #38 in ID3.py and comment line #37..
"# bestAttribute = self.chooseBestAttributeImpurity(trainingValues, Class, Attributes, varianceImpurity)" 


Open Accuracy.txt for report on accuracies on post pruned trees by both heuristics
Open Tree.txt for the tree output

The results are for data_sets1 directory.
For data_sets2, uncomment line #10 in main.py