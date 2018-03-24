class Settings():
	''' store game settings'''
	def __init__(self):
		# screen size
		self.screen_width = 740
		self.screen_height = 740
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