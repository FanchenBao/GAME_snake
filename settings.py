class Settings():
	''' store game settings'''
	def __init__(self):
		# screen size
		self.screen_width = 400
		self.screen_height = 400
		# background color
		self.background_color = (34,139,34)

		# size of unit grid
		self.unit = 20
		# number of ticks per axis
		self.x_ticks = int(self.screen_width / self.unit)
		self.y_ticks = int(self.screen_height / self.unit)
		# create a grid with given x and y coordinates on the axis
		self.x_axis = tuple(range(0, self.screen_width, self.unit))
		self.y_axis = tuple(range(0, self.screen_height, self.unit))
		# flag to determine whether game is active
		self.game_active = False
		self.reset()

	def reset(self):
		# point earned after eating each new body
		self.point = 100
		# flag, recording snake head's new movement from keyboard input
		self.movement = 0