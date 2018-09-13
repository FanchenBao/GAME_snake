'''
Author: Fanchen Bao
Date: 03/20/2018

Description:
Body class, body of the snake. Pay attention to how body changes its movement direction contingent on how the head has been moving.
Since head can change direction multiple times while the body is still traveling in one direction, 
it is necessary to record the direction each time head makes a turn and where the turn is made, so that all bodies can follow suit.
'''

import pygame
from pygame.sprite import Sprite

class Body(Sprite):
	def __init__(self, screen, ai_settings, image_source, index, is_food = False):
		super().__init__()
		''' initiate a class representing each body segment of the snake'''
		self.screen = screen
		self.ai_settings = ai_settings
		self.image_source = image_source
		self.screen_rect = self.screen.get_rect()

		self.index = index

		self.is_food = is_food
		
		if self.is_food:
			self.image = pygame.image.load('images/food.bmp')
		else:
			self.image = self.image_source.body_image_h.copy()
		self.rect = self.image.get_rect()
		# self.rect = pygame.Rect(0, 0, 20, 20)
		# self.color = (0, 0, 0)
		self.rect.x = 0
		self.rect.y = 0

		# record the previous moving direction of snake before initiation of next movement
		self.dir = 0

		# record the list of position where change of direction on head takes place
		self.pos_change = []
		# record the list of new directions that head takes
		self.dir_change = []

	def update(self):
		'''update current position of the body, movement occurs at the increment of each unit'''
		# body does not move until AFTER initial keyboard input
		if self.ai_settings.movement:
			# body position change happens ONLY after head has changed
			if self.dir_change:
				# if head change is going up or down (from a previous horizontal dir)
				if self.dir_change[0] in [1, 3]:
					# record body's current x 
					current_location = self.rect.x
				# if head change is going left or right (from a previous vertical dir)
				if self.dir_change[0] in [2, 4]:
					# record body's current y
					current_location = self.rect.y

				# compare the body's current x or y to the corresponding x or y when head changes
				if current_location == self.pos_change[0]:
					# changes to vertical
					if self.dir_change[0] in [1, 3]:
						self.image = self.image_source.body_image_v.copy()
					# changes to horizontal
					if self.dir_change[0] in [2, 4]:
						self.image = self.image_source.body_image_h.copy()
					# body's new direction is the same as head's new direction
					self.dir = self.dir_change[0]
					# delete the head's direction and its corresponding change position to prepare for next change
					del self.dir_change[0]
					del self.pos_change[0]
			self.move(self.dir)	

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


	# def draw(self):
	# 	self.screen.fill(self.color, self.rect)