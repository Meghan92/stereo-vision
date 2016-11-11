from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
from nolearn.dbn import DBN
import numpy as np
import cv2
import cPickle as pickle
import os


def run(_input, _output):
	dbn = DBN(
		[64, 32, 2],
		learn_rates = 0.3,
		learn_rate_decays = 0.9,
		epochs = 20,
		verbose = 1,
		minibatch_size=1)
	dbn.fit(_input, _output)
	current_path = os.path.dirname(__file__)
	weights_path = os.path.join(current_path, "weights.pkl")
	save_object(dbn, weights_path)


def save_object(obj, filename):
	with open(filename, 'wb') as output:
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)