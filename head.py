import pygame
from pygame.sprite import Sprite

class Head(Sprite):
	def __init__(self, screen, ai_settings, image_source, bodies):
		super().__init__()
		''' initiate a class representing each body segment of the snake'''
		self.screen = screen
		self.ai_settings = ai_settings
		self.image_source = image_source
		self.screen_rect = self.screen.get_rect()

		self.bodies = bodies
		
		self.image = self.image_source.head_image_r.copy()
		self.rect = self.image.get_rect()
		# self.rect = pygame.Rect(0, 0, 20, 20)
		# self.color = (0, 0, 0)
		self.rect.x = self.ai_settings.x_axis[int(self.ai_settings.x_ticks / 2 - 1)]
		self.rect.y = self.ai_settings.y_axis[int(self.ai_settings.y_ticks / 2 - 1)]

		# flags for moving the head
		self.movement = 0

		# record the previous moving direction of snake before initiation of next movement
		self.dir = 0

	def update(self):
		'''update current position of the body, movement occurs at the increment of each unit'''
		# when snake is already moving (thus having a dir already)
		if self.dir:
			# change head direction
			self.change_head_position()
		# move snake from a motionless position (at the beginning of game)
		else:
			for body in self.bodies.sprites():
				body.movement = self.movement
			self.move(self.movement)

	def move(self, direction):
		''' move the snake along the screen (grid)'''
		if direction == 4:
			self.rect.x -= self.ai_settings.unit
			# allow the body to reappear at the opposite side of screen
			if self.rect.left < self.screen_rect.left:
				self.rect.x = self.screen_rect.right
			self.dir = 4
		if direction == 2:
			self.rect.x += self.ai_settings.unit
			# allow the body to reappear at the opposite side of screen
			if self.rect.right > self.screen_rect.right:
				self.rect.x = self.screen_rect.left
			self.dir = 2
		if direction == 3:
			self.rect.y += self.ai_settings.unit
			# allow the body to reappear at the opposite side of screen
			if self.rect.bottom > self.screen_rect.bottom:
				self.rect.y = self.screen_rect.top
			self.dir = 3
		if direction == 1:
			self.rect.y -= self.ai_settings.unit
			# allow the body to reappear at the opposite side of screen
			if self.rect.top < self.screen_rect.top:
				self.rect.y = self.screen_rect.bottom
			self.dir = 1

	def update_head(self):
		''' Update head image to represent rotation without losing pixel,
		also record the direction and location of such change, as reference for the body to follow.'''
		if self.movement == 1:
			# record head x coordinate
			for body in self.bodies.sprites():
				body.pos_change.append(self.rect.x)
			self.image = self.image_source.head_image_u.copy()
		if self.movement == 3:
			# record head x coordinate
			for body in self.bodies.sprites():
				body.pos_change.append(self.rect.x)
			self.image = self.image_source.head_image_d.copy()
		if self.movement == 4:
			# record head y coordinate
			for body in self.bodies.sprites():
				body.pos_change.append(self.rect.y)
			self.image = self.image_source.head_image_l.copy()
		if self.movement == 2:
			# record head y coordinate
			for body in self.bodies.sprites():
				body.pos_change.append(self.rect.y)
			self.image = self.image_source.head_image_r.copy()
		# record the direction of change
		for body in self.bodies.sprites():
			body.dir_change.append(self.movement)
		self.move(self.movement)

	def change_head_position(self):
		''' change head position and move in the new direction'''
		# if head's current direction is the same or opposite to new direction input, do not change course
		if abs(self.movement - self.dir) in [0, 2]:
			self.move(self.dir)
		# only change course when current direction is perpendicular to new input
		else:
			self.update_head()

	def blitme(self):
		self.screen.blit(self.image, self.rect)