class Settings():
	''' store game settings'''
	def __init__(self):
		# screen size
		self.screen_width = 740
		self.screen_height = 740
		# background color
		self.background_color = (255, 255, 255)

		# size of unit grid
		self.unit = 37
		# number of ticks per axis
		self.ticks = 20
		# create a grid with given x and y coordinates on the axis
		self.x_axis = (0, 37, 74, 111, 148, 185, 222, 259, 296, 333, 370, 407, 444, 481, 518, 555, 592, 629, 666, 703)
		self.y_axis = (0, 37, 74, 111, 148, 185, 222, 259, 296, 333, 370, 407, 444, 481, 518, 555, 592, 629, 666, 703)
