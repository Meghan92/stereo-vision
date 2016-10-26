import verification as verify
import recognition as recog


class verification():
	def train(self, resolution):
		verify.train(resolution)
	
	def run(self, resolution):
		verify.run(resolution)


class recognition():

	def train(self):
		recog.train()

	def run(self, username):
		recog.run(username)
