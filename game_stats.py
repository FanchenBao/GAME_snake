class GameStats():
	''' track game statistics'''
	def __init__(self):
		self.reset_stats()
		self.read_high_score()
	
	def reset_stats(self):
		# record current score
		self.score = 0

	def read_high_score(self):
		# read high score
		self.high_score = 0
