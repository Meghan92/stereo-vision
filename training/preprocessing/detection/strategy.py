import convolution.recognition as recognition
import convolution.verification as verification
import detection.count as count


def run():
    if count.faces() > 1:
        return recognition
    else:
        return verification
