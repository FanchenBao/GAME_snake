'''
Author: Fanchen Bao
Date: 03/24/2018

Description:
Button class, for message display
'''

import pygame
import pygame.font

class Button():
	''' create a button to show start-of-game and end-of-game message'''
	def __init__(self, screen, ai_settings, msgs, game_end):
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = self.screen.get_rect()
		self.msgs = msgs
		self.game_end = game_end

		# the unchanging button properties
		self.width = 200
		self.button_color = (0, 0, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 30)
		
		# when game ends
		if self.game_end:
			self.height = 220
		# when game starts
		else:
			self.height = 90
		# position the button at the center of screen
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		if self.game_end:
			# prep message on the button
			self.prep_msg3()
			self.prep_msg1()
			self.prep_msg4()
			self.prep_msg5()
			self.prep_msg6()
			self.prep_msg7()
		else:
			# prep message on the button
			self.prep_msg1()
			self.prep_msg2()

	def prep_msg1(self):
		self.msg1_image = self.font.render(self.msgs[0], True, self.text_color, self.button_color)
		self.msg1_image_rect = self.msg1_image.get_rect()
		self.msg1_image_rect.centerx = self.rect.centerx
		if self.game_end:
			self.msg1_image_rect.centery = self.rect.top + 70
		else:
			self.msg1_image_rect.centery = self.rect.centery - 20
		
	def prep_msg2(self):
		self.msg2_image = self.font.render(self.msgs[1], True, self.text_color, self.button_color)
		self.msg2_image_rect = self.msg2_image.get_rect()
		self.msg2_image_rect.centerx = self.rect.centerx
		self.msg2_image_rect.centery = self.rect.centery + 20

	def prep_msg3(self):
		self.msg3_image = self.font.render(self.msgs[2], True, self.text_color, self.button_color)
		self.msg3_image_rect = self.msg3_image.get_rect()
		self.msg3_image_rect.centerx = self.rect.centerx
		self.msg3_image_rect.y = self.rect.top + 30

	def prep_msg4(self):
		self.msg4_image = self.font.render(self.msgs[3], True, self.text_color, self.button_color)
		self.msg4_image_rect = self.msg4_image.get_rect()
		self.msg4_image_rect.centerx = self.rect.centerx
		self.msg4_image_rect.y = self.rect.top + 110

	def prep_msg5(self):
		self.msg5_image = self.font.render(self.msgs[4], True, self.text_color, self.button_color)
		self.msg5_image_rect = self.msg5_image.get_rect()
		self.msg5_image_rect.centerx = self.rect.centerx
		self.msg5_image_rect.y = self.rect.top + 130

	def prep_msg6(self):
		self.msg6_image = self.font.render(self.msgs[5], True, self.text_color, self.button_color)
		self.msg6_image_rect = self.msg6_image.get_rect()
		self.msg6_image_rect.centerx = self.rect.centerx
		self.msg6_image_rect.y = self.rect.top + 160

	def prep_msg7(self):
		self.msg7_image = self.font.render(self.msgs[6], True, self.text_color, self.button_color)
		self.msg7_image_rect = self.msg7_image.get_rect()
		self.msg7_image_rect.centerx = self.rect.centerx
		self.msg7_image_rect.y = self.rect.top + 180

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		if self.game_end:
			self.screen.blit(self.msg3_image, self.msg3_image_rect)
			self.screen.blit(self.msg1_image, self.msg1_image_rect)
			self.screen.blit(self.msg4_image, self.msg4_image_rect)
			self.screen.blit(self.msg5_image, self.msg5_image_rect)
			self.screen.blit(self.msg6_image, self.msg6_image_rect)
			self.screen.blit(self.msg7_image, self.msg7_image_rect)
		else:
			self.screen.blit(self.msg1_image, self.msg1_image_rect)
			self.screen.blit(self.msg2_image, self.msg2_image_rect)