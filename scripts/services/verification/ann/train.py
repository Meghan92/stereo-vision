from nolearn.lasagne import NeuralNet
from lasagne import layers
from lasagne.updates import nesterov_momentum
import cPickle as pickle
import os
import lasagne


def run(_input, _output):
    dbn = NeuralNet(
        layers=[('input1', layers.InputLayer),
                ('input2', layers.InputLayer),
                ('hidden', layers.DenseLayer),
                ('hidden1', layers.DenseLayer),
                ('output', layers.DenseLayer)],
        # layer parameters:
        input1_shape=(None, 3, 95, 95),
        input2_shape=(None, 3, 95, 95),
        output_nonlinearity=lasagne.nonlinearities.sigmoid,  # output layer uses identity function
        output_num_units=1,  # 2 target values
        hidden_num_units=2000,  # number of units in hidden layer
        hidden1_num_units=1000,  # number of units in hidden layer

        # optimization method:
        update=nesterov_momentum,
        update_learning_rate=0.01,
        update_momentum=0.9,

        regression=True,  # flag to indicate we're dealing with regression problem
        max_epochs=100,  # we want to train this many epochs
        verbose=1,
    )
    dbn.fit({"input": _input[0], "input2": _input[1]}, _output)
    current_path = os.path.dirname(__file__)
    weights_path = os.path.join(current_path, "weights.pkl")
    save_object(dbn, weights_path)


def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def print_report(raw_predictions, expected_output):
    i = 0
    fake_images = []
    real_images = []
    for raw_prediction in raw_predictions:
        raw_prediction = round(raw_prediction)
        if expected_output[i] == -1:
            prediction = 1
            if raw_prediction == 1:  # if a true image is predicted
                prediction = 0  # add prediction count as 0
            fake_images.append(prediction)
        elif expected_output[i] == 1:
            prediction = 1
            if raw_prediction == 0:  # if a fake image is predicted
                prediction = 0  # add prediction count as 0
            real_images.append(prediction)
        else:
            raise ValueError("Unexpected value for expected output: {}".format(expected_output[i]))
        i += 1
    print real_images
    print fake_images
    print "Number of fake images: {}".format(fake_images.__len__())
    print "Number of real images: {}".format(real_images.__len__())
    fake_percentage = round(sum(fake_images) / fake_images.__len__() * 100.0)
    real_percentage = round(sum(real_images) / real_images.__len__() * 100.0)
    print "Percentage accuracy for fake images: {}".format(fake_percentage)
    print "Percentage accuracy for real images: {}".format(real_percentage)
