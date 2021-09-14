import pandas as pd
from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
	return distance.euclidean(a,b)

class CustomKNN():
	def fit(self, trainingdata, trainingtarget):
		self.trainingdata = trainingdata
		self.trainingtarget = trainingtarget

	def predict(self, testdata):
		predictions = []
		for row in testdata:
			label = self.closest(row)
			predictions.append(label)
		return predictions

	def closest(self, row):
		best_dist = euc(row, self.trainingdata[0])
		best_index = 0
		for i in range(1, len(self.trainingdata)):
			dist = euc(row, self.trainingdata[i])
			if dist < best_dist:
				best_dist = dist
				best_index = i
		return self.trainingtarget[best_index]

def KNN():
	iris = load_iris()

	data = iris.data
	target = iris.target

	train_data, test_data, train_target, test_target = train_test_split(data, target, test_size = 0.5)

	classifier = CustomKNN()

	classifier.fit(train_data, train_target)

	predictions = classifier.predict(test_data)

	accuracy = accuracy_score(test_target, predictions)

	return accuracy

def main():
	border = "-" * 50
	print(border)
	accuracy = KNN()
	print("Accuracy of custom KNN: ", accuracy*100)
	print(border)

if __name__ == '__main__':
	main()