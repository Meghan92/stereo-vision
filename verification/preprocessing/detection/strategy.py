import convolution.recognition as recognition
import convolution.verification as verification
import detection.count as count


def run():
	if count.faces() > 1:
		print "- Running recognition"
		return recognition
	else:
		print "- Running verification"
		return verification
