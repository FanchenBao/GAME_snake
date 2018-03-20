import pygame
from pygame.sprite import Sprite

class Body(Sprite):
	def __init__(self, screen, ai_settings):
		super().__init__()
		''' initiate a class representing each body segment of the snake'''
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load('images/body.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = self.ai_settings.x_axis[int(self.ai_settings.ticks / 2 - 1)]
		self.rect.y = self.ai_settings.y_axis[int(self.ai_settings.ticks / 2 - 1)]

		# flags for moving the body
		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False

	def update(self):
		'''update current position of the body, movement occurs at the increment of each unit'''
		if self.move_left:
			self.rect.x -= self.ai_settings.unit
		if self.move_right:
			self.rect.x += self.ai_settings.unit
		if self.move_down:
			self.rect.y += self.ai_settings.unit
		if self.move_up:
			self.rect.y -= self.ai_settings.unit