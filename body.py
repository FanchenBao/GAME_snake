import pygame
from pygame.sprite import Sprite

class Body(Sprite):
	def __init__(self, screen, ai_settings):
		super().__init__()
		''' initiate a class representing each body segment of the snake'''
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = self.screen.get_rect()

		self.width = self.ai_settings.unit
		self.height = self.ai_settings.unit
		self.color = (0, 0, 0)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = self.ai_settings.x_axis[self.ai_settings.ticks/2 - 1]
		self.rect.y = self.ai_settings.y_axis[self.ai_settings.ticks/2 - 1]

		# flags for moving the body
		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False

	def update(self):
		'''update current position of the body'''
		if self.move_left:
			