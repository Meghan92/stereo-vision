import preprocessing.convolution.recognition as recognition
import preprocessing.convolution.verification as verification
import preprocessing.detection.count as count


def run():
    if count.faces() > 1:
        return recognition
    else:
        return verification
