import MySQLdb


class ConnectionString:
	def __init__(self):
		self.database = MySQLdb.connect("localhost", "demo", "D3M0U53R", "StereoVision")
