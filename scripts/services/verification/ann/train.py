from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn import datasets
from sklearn.datasets import fetch_mldata
from nolearn.dbn import DBN
#from nolearn.lasagne import NeuralNet
import numpy as np
import cv2
import cPickle as pickle
import os



def run(_input, _output):
	#mnist = fetch_mldata('MNIST original')
	#x_train, x_test, y_train, y_test = 	train_test_split(mnist.data/255.0, mnist.target)
	x_train, x_test, y_train, y_test = 	train_test_split(_input, _output)
	neuralnet_structure = []
	neuralnet_structure.append(x_train.shape[1])
	for x in range(0, 2):
		neuralnet_structure.append(100)
	neuralnet_structure.append(-1)
	dbn = DBN(
		neuralnet_structure,
		learn_rates = 0.3,
		learn_rate_decays = 0.9,
		epochs = 10,
		verbose = 1,
		minibatch_size=10)
	#dbn = NeuralNet(		
	dbn.fit(x_train, y_train)
	current_path = os.path.dirname(__file__)
	weights_path = os.path.join(current_path, "weights.pkl")
	save_object(dbn, weights_path)
	preds = dbn.predict(x_test)
	print classification_report(y_test, preds)
	print confusion_matrix(y_test, preds)


def save_object(obj, filename):
	with open(filename, 'wb') as output:
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
