from nolearn.dbn import DBN
import numpy as np
import cv2
import cPickle as pickle


def run(_input):
	dbn = read_object()
	preds = dbn.predict(_input)
	return preds[0]


def read_object():
	with open("output/weights.pkl", "rb") as input:
		return pickle.load(input)