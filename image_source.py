'''
Author: Fanchen Bao
Date: 03/22/2018

Description:
Since rotating images in pygame with the image quality I can provide has poor performance, the turning of snake's face is achieved by loading the corresponding face image.
ImageSource class serves this purpose.
'''

import pygame

class ImageSource():
	''' a class to store all the necessary images of the snake body parts facing different directions'''
	def __init__(self):
		# snake head facing right, left, up, and down
		self.head_image_r = pygame.image.load('images/head_r.bmp')
		self.head_image_l = pygame.image.load('images/head_l.bmp')
		self.head_image_u = pygame.image.load('images/head_u.bmp')
		self.head_image_d = pygame.image.load('images/head_d.bmp')
		# snake body vertical and horizontal
		self.body_image_v = pygame.image.load('images/body_v.bmp')
		self.body_image_h = pygame.image.load('images/body_h.bmp')