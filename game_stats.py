class GameStats():
	''' track game statistics'''
	def __init__(self, filename):
		self.filename = filename

		self.reset_stats()
		self.read_high_score()
	
	def reset_stats(self):
		# record current score
		self.score = 0

	def read_high_score(self):
		# read high score
		with open(self.filename) as file_object:
			content = file_object.read()
		self.high_score = int(content)
