from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
from nolearn.dbn import DBN
import numpy as np
import cv2


def run(_input, _output):
	(trainX, testX, trainY, testY) = train_test_split(_input, _output)

	dbn = DBN(
		[64, 32, 2],
		learn_rates = 0.3,
		learn_rate_decays = 0.9,
		epochs = 10,
		verbose = 1)
	dbn.fit(trainX, trainY)

	preds = dbn.predict(testX)
	print classification_report(testY, preds)
