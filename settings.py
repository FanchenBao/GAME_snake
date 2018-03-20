class Settings():
	''' store game settings'''
	def __init__(self):
		# screen size
		self.screen_width = 740
		self.screen_height = 740
		# background color
		self.background_color = (255, 255, 255)

		# size of unit grid
		self.unit = 20
		# number of ticks per axis
		self.ticks = 37
		# create a grid with given x and y coordinates on the axis
		self.x_axis = tuple(range(0, 740, 20))
		self.y_axis = tuple(range(0, 740, 20))
