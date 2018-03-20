import sys
import pygame

def check_events():
	'''monitor user key or mouse input'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_key_down_event()

def check_key_down_event():
	''' determine action based on player keyboard input'''
	if event.key == pygame.K_LEFT:
		