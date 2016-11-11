from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import classification_report, accuracy_score
from sklearn import datasets
from nolearn.dbn import DBN
import numpy as np
import cv2
import cPickle as pickle
import os



def run(_input, _output):

	x_train, x_test, y_train, y_test = 	train_test_split(_input, _output, test_size=0.33, random_state=42)
	dbn = DBN(
		[64, 200, 2],
		learn_rates = 0.3,
		learn_rate_decays = 0.9,
		epochs = 100,
		verbose = 1,
		minibatch_size=1)
	dbn.fit(x_train, y_train)
	current_path = os.path.dirname(__file__)
	weights_path = os.path.join(current_path, "weights.pkl")
	save_object(dbn, weights_path)
	preds = dbn.predict(x_test)
	print classification_report(y_test, preds)


def save_object(obj, filename):
	with open(filename, 'wb') as output:
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
