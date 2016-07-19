from nolearn.dbn import DBN
import numpy as np
import cv2
import cPickle as pickle
import os


def run(_input):
	array = []
	array.append(_input)
	processed = np.array(array)
	dbn = read_object()
	preds = dbn.predict(processed)
	return preds[0]


def read_object():
	current_path = os.path.dirname(__file__)
	output_path = os.path.join(current_path, "output")
	weight_path = os.path.join(output_path, "weights.pkl")
	with open(weight_path, "rb") as input:
		return pickle.load(input)