import pygame
from pygame.sprite import Sprite

class Body(Sprite):
	def __init__(self, screen, ai_settings, image_source, index):
		super().__init__()
		''' initiate a class representing each body segment of the snake'''
		self.screen = screen
		self.ai_settings = ai_settings
		self.image_source = image_source
		self.screen_rect = self.screen.get_rect()

		self.index = index
		
		if self.index == 1:
			self.image = self.image_source.head_image_r.copy()
		else:
			self.image = self.image_source.body_image_h.copy()

		self.rect = self.image.get_rect()
		# self.rect = pygame.Rect(0, 0, 20, 20)
		# self.color = (0, 0, 0)
		self.rect.x = self.ai_settings.x_axis[int(self.ai_settings.x_ticks / 2 - 1)]
		self.rect.y = self.ai_settings.y_axis[int(self.ai_settings.y_ticks / 2 - 1)]

		# flags for moving the body
		self.movement = False
		# record the previous moving direction of snake before initiation of next movement
		self.dir = False

	def update(self):
		'''update current position of the body, movement occurs at the increment of each unit'''
		if self.dir:
			if self.movement == 'left' or self.movement == 'right':
				if self.dir == 'up' or self.dir == 'down':
					self.change_dirction(self.movement)
				else:
					self.move(self.dir)
			if self.movement == 'up' or self.movement == 'down':
				if self.dir == 'right' or self.dir == 'left':
					self.change_dirction(self.movement)
				else:
					self.move(self.dir)
		else:
			self.move(self.movement)

	def move(self, direction):
		''' move the snake along the screen (grid)'''
		if direction == 'left':
			self.rect.x -= self.ai_settings.unit
			# allow the body to reappear at the opposite side of screen
			if self.rect.left < self.screen_rect.left:
				self.rect.x = self.screen_rect.right
			self.dir = 'left'
		if direction == 'right':
			self.rect.x += self.ai_settings.unit
			# allow the body to reappear at the opposite side of screen
			if self.rect.right > self.screen_rect.right:
				self.rect.x = self.screen_rect.left
			self.dir = 'right'
		if direction == 'down':
			self.rect.y += self.ai_settings.unit
			# allow the body to reappear at the opposite side of screen
			if self.rect.bottom > self.screen_rect.bottom:
				self.rect.y = self.screen_rect.top
			self.dir = 'down'
		if direction == 'up':
			self.rect.y -= self.ai_settings.unit
			# allow the body to reappear at the opposite side of screen
			if self.rect.top < self.screen_rect.top:
				self.rect.y = self.screen_rect.bottom
			self.dir = 'up'

	def change_dirction(self, change_type):
		''' change direction of the snake's progression. 
		clockwise: angle = -90; counterclockwise: angle = 90
		from vertical to horizontal, change_type = 1; from horizontal to vertical, change_type = 0'''
		# when change of direction happens, it requires the head to FIRST rotate and then move in the new direction
		if self.index == 1:
			if change_type == 'up':
				self.ai_settings.pos_change = self.rect.x
				self.image = self.image_source.head_image_u.copy()
			if change_type == 'down':
				self.ai_settings.pos_change = self.rect.x
				self.image = self.image_source.head_image_d.copy()
			if change_type == 'left':
				self.ai_settings.pos_change = self.rect.y
				self.image = self.image_source.head_image_l.copy()
			if change_type == 'right':
				self.ai_settings.pos_change = self.rect.y
				self.image = self.image_source.head_image_r.copy()
			self.move(self.movement)
		
		# then the rest of the body must first reach where the head was, then do the same manuever
		else:	
			if change_type == 'up' or change_type == 'down':
				current_location = self.rect.x
			if change_type == 'left' or change_type == 'right':
				current_location = self.rect.y

			if current_location == self.ai_settings.pos_change:
				if change_type == 'up' or change_type == 'down':
					self.image = self.image_source.body_image_v.copy()
				if change_type == 'left' or change_type == 'right':
					self.image = self.image_source.body_image_h.copy()
				self.move(self.movement)
			
			# if the rest of the body hasn't reached where the head was, they shall keep going the same direction as previously
			else:
				self.move(self.dir)


	# def draw(self):
	# 	self.screen.fill(self.color, self.rect)