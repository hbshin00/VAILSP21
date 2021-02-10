from sklearn.datasets import load_iris
from sklearn import tree
import graphviz

#Load in dataset
iris_data = load_iris()

#Initialize decision tree object
classification_tree = tree.DecisionTreeClassifier()

#Train decision tree (tree induction + pruning)
classification_tree = classification_tree.fit(iris_data.data, iris_data.target)

dot_data = tree.export_graphviz(classification_tree, out_file=None,
    feature_names=iris.feature_names, class_names=iris.target_names,
    filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris")
